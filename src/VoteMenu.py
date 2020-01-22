import json
import sys
from src.Config import CONFIG
from src.Helpers import cls
from src.Menu.Menu import Menu
from src.Menu.MenuOption import MenuOption

"""
Esta classe foi criada para organizar tudo o que pretence a votação.
"""


class VoteMenu:
    menu = None

    # Construtor, função a ser chamada quando for instanciado um objeto deste tipo.
    def __init__(self, db):
        self.db = db

    """
    Esta função ira ser chamada quando qualquer programa for escolhido, 
    esse mesmo programa vai ser passado como parametro (program)
    """
    def vote_option_menu_handler(self, program):
        # obter a informação adicional do programa.
        metadata = program.getmetadata()

        # Incrementa votos do programa
        metadata['votes'] = int(metadata['votes']) + 1
        print(program.name)
        # Atualizar programa na base de dados
        self.db.update('programs', data={"votes": metadata['votes']}, where="name = '%s'" % program.name)

        # clear no screen.
        cls()
        # las but not least, apresentar o menu.
        self.menu.show()
        input()

    """
    Função que calcula a percentagem de votos de cada programa, 
    como é pedido no enunciado Ultimo ponto.
    """
    def __calc_program_votes(self, pvotes, totalvotes):
        return round((pvotes / totalvotes) * 100, 1)

    """
    Criar a barrinha de percentagem para cada linha de votos.
    """
    def __build_progressbar(self, percent):
        max_blocks = 19
        # Calcular quandos quadradinhos imprimir para cada percentagem de votos
        how_many_chars = int(round(((max_blocks * percent) / 100), 1) + 1)

        return CONFIG.PROGRESSBARCHAR * how_many_chars


    """
    Construir tabela de votos conforme os programas;
    Esta função chamada quando a votação terminar;
    """
    def __build_list_table(self, items):

        print("▬" * 80)

        # Apresentar cabeçalho da tabela de votos.
        print('{:<36}{:<17}{:<3}'.format("Nome", "Nº Votos", "Nº Votos(%)"))
        print("▬" * 80)

        # soma total de todos os votos
        total = sum([p.getmetadata('votes') for p in items])

        """
        Iterar todos os programas e apresentar linha a linha.
        Será calculado a percentagem de cada program aqui e apresentar o mesmo.
        """
        for program in items:

            metadata = program.getmetadata()

            # saltar para o proximo programa quando o nº de votos for 0.
            if metadata['votes'] == 0:
                continue

            # Calcular percentagem de votos de cada programa
            percent = self.__calc_program_votes(metadata['votes'], total)

            # Definir formatação para cada linha na tabela de votos.
            line_str = "%s) %s" % (program.getid(), program.getname())

            # Apresentar a linha com tabulação e limite de 34, 17, 3 caracteres.
            print('{:<36}{:<17}{:<3}'.format(line_str, metadata['votes'], "%s %.1f%%" % (self.__build_progressbar(percent), percent)))

        print("▬" * 80)
        input()


    """
    Quando a opção de saida do menu** for clicada esta função ira ser chamada.
    ** self.menu.setmenu_close(callback=self.menu_close_handler, choice=0)
    
    Ou seja, quando o choice (0) for escolhido no menu esta função vai ser chamada automaticamente
    """
    def menu_close_handler(self, items):
        # limpar ecrã
        cls()

        # apresentar a tabela
        self.__build_list_table(items)

        # fechar programa
        sys.exit()

    """
    Esta função vai ser chamada quando a formatação do menu ocorrer, 
    deverá retornar uma string contendo a formatação de cada item do menu
    """
    def format_menu_option(self, item):
        # obter horario do programa especifico.
        schedule = json.loads(item.getmetadata()['schedule'])

        schedule_end = schedule.get('end', '00')
        schedule_start = schedule.get('start', '00')

        # 1: Programa da Joana (18h-20h)
        return "%s: %s (%sh-%sh)" % (item.getid(), item.getname(), schedule_start, schedule_end)

    """
    Este metodo vai ser chamado quando programa iniciar em 'modo normal',
    neste caso sem o paramentro --admin.
    """
    def show(self, data):
        self.menu = Menu(CONFIG.NAME, subtitle=CONFIG.SUBTITLE)

        # Construir todas as opções do programa
        for index, program in enumerate(data):

            # definir uma estrutura de dados para o metadata(informação adicional) de cada opção do menu.
            metadata = {
                "schedule": program.schedule,
                "votes": program.votes,
                "id": program.id
            }

            # Adicionar item ao menu
            self.menu.add_item(
                MenuOption(id=index+1, name=program.name, metadata=metadata, callback=self.vote_option_menu_handler)
            )

        # Definir função a ser chamada quando choice for escolhido no menu.
        self.menu.setmenu_close(callback=self.menu_close_handler(self.menu.items), choice=0)

        # Definir função a ser chamada quando ocorrer a formatação de cada opção do menu.
        self.menu.setformat_menu_option(self.format_menu_option)

        # Last but not least, apresentar menu.
        self.menu.show()
