from consolemenu import *
from consolemenu.items import *

"""
Classe é uma abstração da dependencia 'console-menu'
Esta classe foi desenvolvida para ajudar na criação de menus em toda a aplicação.
"""


class MenuBuilder:
    menu = ''

    # Construtor da classe Menu
    def __init__(self, title, subtitle):
        # Guardar instancia de menu como uma propiedade.
        self.menu = ConsoleMenu(title, subtitle)
        self.menu.formatter.set_top_margin(0)

    def add_selection_item(self, title, items):
        # Criar seleção de menu de items.
        selection_menu_items = SelectionMenu([])

        # Adicionar a seleção de items ao uma sub-lista
        submenu_item = SubmenuItem(title, selection_menu_items, self.menu)

        selection_menu_items.append_item(SelectionItem(2, 3, self.menu))

        # Adicionar sub-lista de itens ao menu.
        return self.menu.append_item(submenu_item)

    def show(self):
        return self.menu.show()
