# coding=utf-8

class MenuOption:

    def __init__(self, id, name, **kwargs):

        # Verificar se id existe e nao é vazio
        if id is (None or str()):
            raise Exception("ID é obrigatório para adicionar uma opção!")

        # Verificar se o nome existe e não é vazio
        if name is (None or str()):
            raise Exception("Nome é obrigatório para adicionar uma opção!")

        self.id = str(id)
        self.name = str(name)
        self.callback = kwargs.get('callback', None)
        self.metadata = kwargs.get('metadata', None)

    def getid(self):
        return self.id

    def getname(self):
        return self.name

    def getcallback(self):
        return self.callback

    def getmetadata(self, key=None):

        if key is not None:
            return self.metadata[key]

        return self.metadata

    def setmetadata(self, metadata):
        self.metadata = metadata

