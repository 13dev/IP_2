import json
import os
import sys
from src.Helpers import cls

"""
Esta classe foi criada para organizar tudo o que pretence ao administrador.
"""
class AdminMenu:
    menu = None

    # Construtor, função a ser chamada quando for instanciado um objeto deste tipo.
    def __init__(self, db):
        self.db = db

    def vote_option_menu_handler(self, program):
        metadata = program.getmetadata()

        metadata['votes'] = int(metadata['votes']) + 1

        self.db.update('programs', data={"votes": metadata['votes']}, where="id = %s" % program.id)

        #program.setmetadata(metadata)
        cls()
        self.menu.show()

    def menu_close_handler(self):
        pass

    def format_menu_option(self, item):

        schedule = json.loads(item.getmetadata()['schedule'])

        schedule_end = schedule.get('end', '00')
        schedule_start = schedule.get('start', '00')

        return "%s: %s (%sh-%sh)" % (item.getid(), item.getname(), schedule_start, schedule_end)

    def show(self, data):
        os.execl(sys.executable, sys.executable, *sys.argv)

        # self.menu = Menu(CONFIG.NAME, subtitle="Modo Administrador.")

        # self.menu.setmenu_close(callback=self.menu_close_handler, choice=0)
        # self.menu.setformat_menu_option(self.format_menu_option)
        #
        #     # Adicionar item ao menu
        #     self.menu.add_item(
        #         MenuOption(id=program.id, name=program.name, metadata=metadata, callback=self.vote_option_menu_handler)
        #     )
        #
        # self.menu.show()
