from view.menu import Menu

class ConsoleView():
    def  __init__(self):
        self.menu = Menu()
        self.work = True

    def start_application(self):
        print("Заметки")
        while(self.work):
            self.menu.print_main_menu()
            number = int(input("Введите номер команды:"))
            if number == 3:
                self.finish()
            else:
                self.menu.execute(number)

    def finish(self):
        print("Выход")
        self.work = False



            

        
            

