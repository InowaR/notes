from presenter.presenter import Presenter
from view.menu import Menu

class ConsoleView():
    def  __init__(self):
        self.menu = Menu()
        self.presenter = Presenter()
        self.work = True

    def start_application(self):
        print("Заметки")
        while(self.work):
           self.menu.print_main_menu()
           self.execute_command()

    def finish(self):
        print("Выход")
        self.work = False

    def execute_command(self):
        command = int(input("Введите номер команды: "))
        if command == 0:
            self.menu.print_find_note_menu()
            command = int(input("Введите номер команды: "))
            if command == 0:
                self.menu.print_main_menu()
            if command == 1:
                self.presenter.find_note_by_id()
        elif command == 1:
            print(self.presenter.show_all_notes())
        elif command == 2:
            self.presenter.create_note()

        elif command == 6:
            self.finish()

            

        
            

