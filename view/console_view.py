from view.menu import Menu

class ConsoleView():
    def  __init__(self):
        self.menu = Menu()
        self.work = True

    def start_application(self):
        print("Заметки")
        self.menu.add_commands_to_main_menu()
        self.menu.add_commands_to_find_note_menu()
        while(self.work):
           self.menu.print_main_menu()


    def finish(self):
        print("Выход")
        self.work = False

    def execute(self):
        number = int(input("Введите номер команды:"))
        self.menu.execute_main_menu_command(number)



            

        
            

