from src.Config import CONFIG
from src.Database import DB
from src.Helpers import cls
from src.VoteMenu import VoteMenu
import sys
from time import sleep


class DefaultMode:
    votemenu = None

    def __init__(self, db):
        self.db = db
        self.votemenu = VoteMenu(self.db)

    def __del__(self):
        self.db.close()
        del self.db
        del self.votemenu

    @staticmethod
    def show_logo():
        ascii_art = """
         __  ___  __                 __   ___    __
        |__)  |  |__) __  |\/|  /\  |  \ |__  | |__)  /\\
        |  \  |  |        |  | /~~\ |__/ |___ | |  \ /~~\\
        """

        for char in ascii_art:
            sleep(.01)
            sys.stdout.write(char)
            sys.stdout.flush()
        sleep(2)
        cls()

    def show(self):
        #Mostrar o logo do programa
        #self.show_logo()

        self.db.update('programs', {"votes": 1, "name": "Festival RTP Canção"}, where="id = 2")
        programs = self.db.fetch('programs', where="id > 0 and id <=20")

        # Mostrar o votemenu com os programas na existentes na base de dados
        # que cumprem a sql montada acima.
        self.votemenu.show(programs)