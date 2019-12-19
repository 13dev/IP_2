from src.Helpers import obj

# Configurações globais
CONFIG = {
    'DB' : {
        'FILENAME': 'database.sqlite3',
        'USER': '',
        'PASSWORD': '',
    }
}

# Passar dicionario como keyworded argumento
# ou seja A=1, B=2
# inves de acessarmos DB['FILENAME'] passa DB.FILENAME,
# para facilitar leitura do codigo e organização
CONFIG = obj(**CONFIG)