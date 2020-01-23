# coding=utf-8
from collections import namedtuple
import os
from src.Menu.MenuOption import MenuOption

"""
Esta classe converte dicionario para objecto

exemplo:

dict = {'a': 'b'}
dict = obj(dict)

print(dict.a)
#Return: b

Classe retira de: https://stackoverflow.com/a/1305682
"""

class obj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, obj(b) if isinstance(b, dict) else b)


"""
Esta classe é uma ajuda para mapear os dados da base de dados.
Exemplo:

(1, 'Preço certo') -> (id=1, name='Preço certo')

irá mapear para uma namedtuple, que é basicamente um tuplo com indices nomeados
"""
def row_factory(cursor, row):
    """Retorna linhas sqlite como tuplas nomeadas."""
    fields = [col[0] for col in cursor.description]
    Row = namedtuple("Row", fields)
    return Row(*row)


"""
Esta função é usada para limpar a consola, em ambos os sistemas operativos
Windows
Linux
"""
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def populateprograms(db, programs):

    for index, p in enumerate(db.fetch_all('programs')):
        programs.append(MenuOption(id=index + 1, name=p.name, metadata={"id": p.id}))

    return programs