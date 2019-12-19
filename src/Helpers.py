from collections import namedtuple


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
"""
def row(cursor, row):
    """Retorna linhas sqlite como tuplas nomeadas."""
    fields = [col[0] for col in cursor.description]
    Row = namedtuple("Row", fields)
    return Row(*row)