# coding=utf-8
from src.Menu.JsonHandler import JsonHandler
from src.Menu.MenuOption import MenuOption


class Menu:
    CHAR = "▬"

    def __init__(self, name, **kwargs):
        self.items = []
        self.name_menu = name
        self.optionid_close = None
        self.optionclose_callback = None
        self.format_menu_option = None
        # definir subtitle para menu
        self.subtitle = kwargs.get('subtitle', None)

        # Paramentro opcional
        self.handler = kwargs.get('handler', None)
        if self.handler is not None:
            # se a função 'read_json' estiver definida no menu_handler, então
            # Chama, obtem retorno e chama a função read_json.
            try:
                file_name = getattr(self.handler, 'read_json')
                # Chamar read_json com nome do arquivo definido no read_json do menu_handler
                self.read_json(file_name(self.handler))

            except AttributeError:
                pass

        self.loop = True

    """
    Esta função anonima irá escolher qual callback chamar
    se o menuHandler no construtor estiver definido, irá chamar lá do mesmo ex:
    retorno = MenuHandler.item1()
    
    se não estiver definido irá chamar definido na funcao add item ex:
    menu.add_item(id=1, name=Opção, callback=função)
    retorno = função()
    
    quando retorno for True o menu irá fechar.
    """
    def __handle_callback(self, item):
        # Foi definido um menu handler?
        if self.handler is not None:
            # Obter uma atributo de um objeto getattr(x, 'y') é equivalente a: x.y
            try:

                callback = getattr(self.handler, str(item.getcallback()))

                # chamar o callback, e obter o retorno
                # callback(self.menuHandler) é igual a: MenuHandler.{função_dinamica}(self)
                return callback(self.handler, item)
            except AttributeError:
                # Apanhar a exception se a função não existir então, alertar.
                raise Exception("A função <%s> não existe no handler Especificado." % item.getcallback())

        else:
            # Obter a 3 posicição que será uma string (nome da função a ser chamada)
            callback = item.getcallback()

            if callable(callback):
                return callback(item)

    def add_item(self, item):
        # verificar se o ID já existe no menu
        if self.__is_on_items(item.getid()):
            raise Exception("O ID <%s> já existe no menu!" % item.getid())

        # Adicionar ao menu
        self.items.append(item)

    def read_json(self, name):
        # fazer o parse do ficheiro
        menus_json = JsonHandler.file(filename=name)

        # Adicionar todas as opções ao Menu
        for option in menus_json:
            callback = option.get('callback', None)
            metadata = option.get('metadata', None)
            self.add_item(
                MenuOption(option['id'], option['name'], callback=callback, metadata=metadata)
            )

    def show(self):
        # Mostrar a divisão do menu
        print(30 * self.CHAR, self.name_menu, 30 * self.CHAR)

        # Mostrar o subtitlo do menu, se tiver
        if self.subtitle is not None:
            print(self.subtitle + "\n")

        for item in self.items:
            # Verificar se existe a função format_menu_option no menu Handler,
            # se sim, chama a mesma, caso contrario, usa um print default
            try:
                format_menu_option = getattr(self.handler, "format_menu_option")
                print(format_menu_option(self.handler, item))
            except AttributeError:
                # Verificar se a função format_menu_option() foi chamada, e chamar o callback
                if self.format_menu_option is not None:
                    print(self.format_menu_option(item))
                else:
                    print("{}: {}".format(item.getid(), item.getname()))

        # Mostrar divisão do menu
        print(78 * self.CHAR)

        while self.loop:
            choice = str(input("Escolha [1-%s]: " % len(self.items)))

            # Verificar se setmenu_close foi chamado e se corresponde ao paremetro choice.
            if choice == str(self.optionid_close) and self.optionid_close is not None:
                # chamar callback definido em setmenu_close.
                self.optionclose_callback()
                # Parar loop
                self.loop = False
            elif not self.__is_on_items(choice):
                print("Opção invalida, tente novamente!")
                continue

            for item in self.items:
                # Verificar se o id do menu e o callback pode ser chamado e se há callback
                if item.getid() == choice and item.getcallback() is not None:
                    # chamar o callback, e obter o retorno
                    should_stop = self.__handle_callback(item)

                    # se o callback retornar true então para o while
                    if should_stop is True:
                        self.loop = False
                    break

    # verificar se uma opção ja existe no menu
    def __is_on_items(self, itemid):
        return itemid in [i.getid() for i in self.items]

    """
    Chamar um callback(função) quando choice for escolhido no menu.
    """
    def setmenu_close(self, callback, choice):
        self.optionclose_callback = callback
        self.optionid_close = choice

    def setformat_menu_option(self, format_menu_option):
        self.format_menu_option = format_menu_option





