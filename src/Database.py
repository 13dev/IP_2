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
        cursor.execute("SELECT %s FROM `%s`" % (fields, table))

        return cursor.fetchall()

    """
    Fecha a conexão a base de dados e elimina o objecto db para libertar memoria
    """
    def close(self):
        self.db.close()
        del self.db