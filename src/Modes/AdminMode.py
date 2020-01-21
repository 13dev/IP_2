import os
import sys

from src.AdminMenu import AdminMenu
from src.Config import CONFIG


class AdminMode:
    db = None
    menu = None

    def __init__(self, db):
        self.db = db
        self.db.open(CONFIG.DB.FILENAME)
        self.menu = AdminMenu(self.db)

    def __del__(self):
        self.db.close()
        del self.db


    def show(self):
        os.startfile(sys.argv[0])