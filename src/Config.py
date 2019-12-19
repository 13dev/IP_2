from src.Helpers import obj

# Configurações globais
CONFIG = {
    'DB' : {
        'FILENAME': 'database.sqlite3',
        'USER': '',
        'PASSWORD': '',
    }
}

# Passar dicionario como keyworded
# ou seja A=1, B=2
CONFIG = obj(**CONFIG)