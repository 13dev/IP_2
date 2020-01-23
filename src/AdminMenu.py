import json
import sys
import time
from src.Config import CONFIG
import subprocess

from src.Helpers import cls, populateprograms
from src.Menu.Menu import Menu
from src.Menu.MenuOption import MenuOption

"""
Esta classe foi criada para organizar tudo o que pretence ao administrador.
"""


class AdminMenu:
    menu = None
    programs = []
    programsids = []

    # Construtor, função a ser chamada quando for instanciado um objeto deste tipo.
    def __init__(self, db):
        self.db = db
        populateprograms(self.db, self.programs)

        self.programsids = [int(p.getid()) for p in self.programs]

    """"
    Esta função ira ser chamada quando qualquer opção for escolhida, 
    esse mesma opção vai ser passada como parametro (option)
    """
    def handle_menu_exit(self, option):
        # voltar para modo normal, se a opção for para sair.
        subprocess.Popen('python Main.py', creationflags=subprocess.CREATE_NEW_CONSOLE)
        sys.exit()

    def handle_add_program(self, option):
        if len(self.programsids) >= CONFIG.LIMIT_PROGRAMS:
            print("Número de programas máximo atingido.")
            time.sleep(2)
            cls()
            # Mostrar menu principal
            self.show()

        nome = str(input("Nome do Programa: "))
        schedule_start = int(input("Hora de Início (24h):"))
        schedule_end = int(input("Hora de Fim (24h):"))

        # Montar estrutura do horario para inserir como string na coluna 'schedule'
        schedule = json.dumps({'start': schedule_start, 'end': schedule_end})

        # Inserir na base de dados
        self.db.insert('programs', data={
            "name": nome,
            "schedule": schedule,
            "votes": 0
        })

        # atualizar programas
        populateprograms(self.db, self.programs)

        cls()
        print("Programa inserido com sucesso!")
        time.sleep(3)
        cls()

        # Mostrar menu principal
        self.show()

    def handle_remove_program(self, option):

        cls()

        print(30 * CONFIG.MENUCHAR, CONFIG.NAME, 30 * CONFIG.MENUCHAR)

        for index, program in enumerate(self.programs):
            print("%s) %s" % (program.getid(), program.getname()))

        print(76 * CONFIG.MENUCHAR)

        loop = True
        while loop:
            choice = int(input("Programa a remover [1-%s]: " % len(self.programs)))

            # Verifica se opção é valida.
            if not(choice in self.programsids):
                print("Opção invalida tente novamente.")
                continue

            program_to_delete = self.findprogrambyid(choice).getmetadata('id')

            self.db.delete('programs', where="id = %s" % program_to_delete)
            loop = False

        # atualizar programas
        populateprograms(self.db, self.programs)

        print()
        print("Removido com sucesso!")
        print()
        time.sleep(1)

        self.show()

        # schedule = json.loads(item.getmetadata()['schedule'])
        #
        # schedule_end = schedule.get('end', '00')
        # schedule_start = schedule.get('start', '00')
        #
        # return "%s: %s (%sh-%sh)" % (item.getid(), item.getname(), schedule_start, schedule_end)

    def show(self):
        self.menu = Menu(CONFIG.NAME, subtitle="Modo Administrador.")

        # Adicionar item ao menu
        self.menu.add_item(
            MenuOption(id="1", name="Adicionar programas televisivos.", callback=self.handle_add_program))
        self.menu.add_item(
            MenuOption(id="2", name="Remover programas televisivos.", callback=self.handle_remove_program))
        self.menu.add_item(
            MenuOption(id="3", name="Sair.", callback=self.handle_menu_exit))

        self.menu.show()

    def findprogrambyid(self, id):
        for p in self.programs:
            if id == int(p.getid()):
                return p

        raise Exception("Programa não encontrado!")
