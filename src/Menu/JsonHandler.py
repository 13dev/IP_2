import json


class JsonHandler:
    filename = ''

    def __init__(self, filename):
        self.filename = filename

    @staticmethod
    def file(**kwargs):
        filename = kwargs.get('filename', None)

        if filename is None:
            filename = JsonHandler.filename

        # Abrir ficheiro
        with open(filename) as json_data:
            # fazer o parse do ficheiro
            return json.load(json_data)
