from presenter.presenter import Presenter
from view.menu import Menu

class ConsoleView():
    def  __init__(self):
        self.presenter = Presenter()
        self.menu = Menu()
        self.work = True

    def start_application(self):
        print("Заметки")
        self.menu.add_commands_to_main_menu()
        self.menu.add_commands_to_find_note_menu()
        while(self.work):
           self.menu.print_main_menu()
           self.execute()

    def finish(self):
        print("Выход")
        self.work = False

    def execute(self):
        number = int(input("Введите номер команды:"))
        if number == 0:
            self.menu.print_find_note_menu()
            number = int(input("Введите номер команды:"))
            if number == 0:
                self.find_note_by_id()
            elif number == 1:
                pass
        elif number == 1:
            self.show_notes()
        elif number == 2:
            self.create_note()
        elif number == 3:
            self.finish()
        else:
            print("Ошибка")
        
    def create_note(self):
        self.presenter.create_note()

    def show_notes(self):
        self.presenter.show_all_notes()

    def find_note_by_id(self):
        self.presenter.find_note_by_id()



            

        
            

