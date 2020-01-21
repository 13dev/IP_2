import json

from src.Helpers import cls
from src.Menu.Menu import Menu
from src.Menu.MenuOption import MenuOption


class VoteMenu:
    menu = None

    def __init__(self, db):
        self.db = db

    def vote_option_menu_handler(self, program):
        metadata = program.getmetadata()

        metadata['votes'] = int(metadata['votes']) + 1

        self.db.update('programs', data={"votes": metadata['votes']}, where="id = %s" % program.id)

        program.setmetadata(metadata)
        cls()
        self.menu.show()

    def menu_close_handler(self):
        print("Fechar votação")

    def format_menu_option(self, item):

        schedule = json.loads(item.getmetadata()['schedule'])

        schedule_end = schedule.get('end', '00')
        schedule_start = schedule.get('start', '00')

        return "%s: %s (%sh-%sh)" % (item.getid(), item.getname(), schedule_start, schedule_end)

    def show(self, data):
        self.menu = Menu("RTP \N{COPYRIGHT SIGN} - Madeira", subtitle="Os Melhores programas televisivos")

        for program in data:
            metadata = {
                "schedule": program.schedule,
                "votes": program.votes
            }

            self.menu.setmenu_close(callback=self.menu_close_handler, choice=0)
            self.menu.setformat_menu_option(self.format_menu_option)

            # Adicionar item ao menu
            self.menu.add_item(
                MenuOption(id=program.id, name=program.name, metadata=metadata, callback=self.vote_option_menu_handler)
            )

        self.menu.show()
