from src.AdminMenu import AdminMenu
from src.Config import CONFIG
from src.Menu.MenuOption import MenuOption


class AdminMode:
    db = None
    menu = None

    def __init__(self, db):
        self.db = db
        self.db.open(CONFIG.DB.FILENAME)

        programs = []
        for index, p in enumerate(self.db.fetch_all('programs')):
            programs.append(MenuOption(id=index+1, name=p.name, metadata={"id": p.id}))

        self.menu = AdminMenu(self.db, programs)


    def __del__(self):
        self.db.close()
        del self.db


    def show(self):

        # Mostrar o votemenu com os programas na existentes na base de dados
        # que cumprem a sql montada acima.
        self.menu.show()

