"""
Esta classe converte dicionario para objecto

exemplo:

dict = {'a': 'b'}
dict = obj(dict)

print(dict.a)
#Return: b
"""


class obj:
    def __init__(self, **entries):
        self.__dict__.update(entries)