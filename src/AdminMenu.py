import json
import sys
import time

from src.Config import CONFIG
import subprocess

from src.Helpers import cls
from src.Menu.Menu import Menu
from src.Menu.MenuOption import MenuOption

"""
Esta classe foi criada para organizar tudo o que pretence ao administrador.
"""
class AdminMenu:
    menu = None

    # Construtor, função a ser chamada quando for instanciado um objeto deste tipo.
    def __init__(self, db):
        self.db = db

    """"
    Esta função ira ser chamada quando qualquer opção for escolhida, 
    esse mesma opção vai ser passada como parametro (option)
    """
    def handle_menu_exit(self, option):
        # voltar para modo normal, se a opção for para sair.
        subprocess.Popen('python Main.py', creationflags=subprocess.CREATE_NEW_CONSOLE)
        sys.exit()

    def handle_add_program(self, option):
        programsids = self.db.fetch_all('programs', fields=['id'])
        if len(programsids) >= CONFIG.LIMIT_PROGRAMS:
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
        cls()
        print("Programa inserido com sucesso!")
        time.sleep(3)
        cls()

        # Mostrar menu principal
        self.show()

    def handle_remove_program(self, option):

        cls()

        print(30 * CONFIG.MENUCHAR, CONFIG.NAME, 30 * CONFIG.MENUCHAR)

        programs = self.db.fetch_all('programs')

        programsids = {i+1: str(v.id) for i, v in enumerate(programs)}

        for index, program in enumerate(programs):
            print("%s) %s" % (index+1, program.name))

        print(76 * CONFIG.MENUCHAR)

        loop = True
        while loop:
            choice = int(input("Programa a remover [1-%s]: " % len(programs)))

            # Verifica se opção é valida.
            if not(choice in programsids.keys()):
                print("Opção invalida tente novamente.")
                continue

            self.db.delete('programs', where="id = %s" % programsids[choice])
            loop = False

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
