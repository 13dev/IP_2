from src.Config import CONFIG
from src.Database import DB
from src.Modes.AdminMode import AdminMode

db = DB()
db.open(CONFIG.DB.FILENAME)

adminmode = AdminMode(db)
adminmode.show()

del adminmode