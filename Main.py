import sys

from src.Config import CONFIG
from src.Database import DB
from src.Modes.DefaultMode import DefaultMode
db = DB()
db.open(CONFIG.DB.FILENAME)

if not('--no-reset' in sys.argv):
    # Dar reset nos votos todos apenas se a opção --no-reset nao existir
    db.update('programs', {"votes": 0})

defaultmode = DefaultMode(db)
defaultmode.show()

#del defaultmode





