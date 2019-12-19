from src.Database import DB
from src.Config import CONFIG

db = DB()
db.open(CONFIG.DB.FILENAME)

programas = db.fetch_all('programs', ['id', 'name'])

print(programas[0].name)

db.close()


#sys.exit()

