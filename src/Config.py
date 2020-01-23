# coding=utf-8
from src.Helpers import obj

# Configurações globais
CONFIG = {
    'DB' : {
        'FILENAME': 'database.sqlite3',
        #'USER': '',
        #'PASSWORD': '',
    },
    'NAME': 'RTP-MADEIRA \N{COPYRIGHT SIGN}',
    'PROGRESSBARCHAR': '■',
    'MENUCHAR': '▬',
    'LIMIT_PROGRAMS': 20,
    'SUBTITLE': "Os Melhores programas televisivos",
}

# Passar dicionario como keyworded argumento
# ou seja A=1, B=2
# inves de acessarmos DB['FILENAME'] passa DB.FILENAME,
# para facilitar leitura do codigo e organização
CONFIG = obj(CONFIG)