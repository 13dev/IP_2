from src.Config import CONFIG
from src.Database import DB
from src.Modes.DefaultMode import DefaultMode
db = DB()
db.open(CONFIG.DB.FILENAME)

defaultmode = DefaultMode(db)
defaultmode.show()
del defaultmode





