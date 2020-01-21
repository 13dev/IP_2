from src.Database import DB
from src.Config import CONFIG
from src.VoteMenu import VoteMenu

db = DB()
db.open(CONFIG.DB.FILENAME)

db.update('programs', {"votes": 1, "name": "Festival RTP Canção"}, where="id = 2")

programs = db.fetch('programs', where="id > 0 and id <=20")

votemenu = VoteMenu(db)
votemenu.show(programs)

db.close()

# ascii_art = """
#  __  ___  __                 __   ___    __
# |__)  |  |__) __  |\/|  /\  |  \ |__  | |__)  /\
# |  \  |  |        |  | /~~\ |__/ |___ | |  \ /~~\
# """
#
# for char in ascii_art:
# 	sleep(.01)
# 	sys.stdout.write(char)
# 	sys.stdout.flush()

print()
print()


#sys.exit()



