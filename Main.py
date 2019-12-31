from src.Database import DB
from src.Config import CONFIG
from src.MenuBuilder import MenuBuilder
import sys
from time import sleep
from src.Helpers import *
import time
from console_progressbar import ProgressBar

db = DB()
db.open(CONFIG.DB.FILENAME)

programas = db.fetch_all('programs', ['id', 'name'])

#print()

db.close()

cls()
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

# pb = ProgressBar(total=100, suffix='completo', decimals=0, length=40, fill='█', zfill='▬')
#
# for i in range(101):
#     pb.print_progress_bar(i)
#     if i == 25 or i == 80 or i == 93:
#         time.sleep(.5)
#
#     time.sleep(.03)
#
# time.sleep(2)

subtitle = "MODO1"
menu = MenuBuilder(CONFIG.NAME, subtitle)

menu.add_selection_item("Votar", {2: 34})
menu.show()
sleep(2)
menu.menu.exit()
# cls()
subtitle = "ALAL"
# menu = MenuBuilder(CONFIG.NAME, subtitle)
# menu.show()


#sys.exit()



