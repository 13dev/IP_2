from src.Config import CONFIG
from src.Database import DB
from src.Modes.DefaultMode import DefaultMode
from src.Modes.AdminMode import AdminMode
import sys

db = DB()
db.open(CONFIG.DB.FILENAME)

adminmode = None
defaultmode = None

# Verificar se existe um argumento --admin na execução do script.
if '--admin' in sys.argv:
    adminmode = AdminMode(db)
    adminmode.show()
else:
    defaultmode = DefaultMode(db)
    defaultmode.show()

if adminmode is not None:
    del adminmode

if defaultmode is not None:
    del defaultmode





