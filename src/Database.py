# coding=utf-8
import sqlite3
from src.Helpers import row_factory

"""
Esta classe foi criada para ajudar a centralizar a conexeção e gereciamento de dados. 
Abstrai grande parte das funções do pacote 'sqlite3' para facilitar desenvolvimento.
"""


class DB:
    db = ''

    """
    Abre a conexão a base de dados
    @param filename - nome do ficheiro onde base de dados se encontra.
    """
    def open(self, filename):
        # Abrir conexão com a base de dados
        self.db = sqlite3.connect(filename)

        """
        Definir o campo row_factory, para que os campos venham nomeados na base de dados.
        função row() importada do Helpers.py, dar uma vista de olhos.
        """
        self.db.row_factory = row_factory

    """
    Obter todos os registos da base de dados
    @param table - tabela a ser selecionada
    @param fields - fields a ser selecionados, irá selecionar todos como padrão
    """
    def fetch_all(self, table, fields="*"):

        """
        Verificar se 'fields é um array, se sim, junta todos os elementos ex:
        ['name', 'email'] -> 'name, email'
        """

        if isinstance(fields, list):
            fields = ', '.join(fields)


        cursor = self.db.cursor()
        cursor.execute("SELECT %s FROM `%s` " % (fields, table))

        return cursor.fetchall()

    """
    Obter todos os registos da base de dados
    @param table - tabela a ser selecionada
    @param where - condição a ser passada para a WHERE do sql.
    @param fields - fields a ser selecionados, irá selecionar todos como padrão
    """
    def fetch(self, table, where, fields="*"):

        """
        Verificar se 'fields é um array, se sim, junta todos os elementos ex:
        ['name', 'email'] -> 'name, email'
        """

        if isinstance(fields, list):
            fields = ', '.join(fields)

        cursor = self.db.cursor()
        cursor.execute("SELECT %s FROM `%s` WHERE %s" % (fields, table, where))

        return cursor.fetchall()

    """
    Fazer update de registo(s) na base de dados
    
    @param table - tabela a ser selecionada
    @param data:dict - cada key corresponde a uma coluna e value a um valor a ser atualizado ex:
        {"coluna1": "valor1", "nome": "NovoNome", "votos": 2}
        
    @param where - adicionar condição de atualização
    """
    def update(self, table, data, where=None):

        sql = "UPDATE %s SET " % table

        values = ()
        cols = []

        for col, value in data.items():
            values += (value,)
            cols.append("%s = ?" % col)

        sql += ', '.join(cols)

        """
        Variavel sql terá o seguinte formato:
        UPDATE programas SET nome = ?, votos = ? WHERE id = ?
        """

        # verificar se condição existe caso contrario irá atualizar todos.
        if where is not None:
            sql += " WHERE %s" % where

        cur = self.db.cursor()
        cur.execute(sql, values)
        self.db.commit()


    """
    Fecha a conexão a base de dados e elimina o objecto db para libertar memoria
    """
    def close(self):
        self.db.close()
        del self.db