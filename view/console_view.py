from view.menu import Menu

class ConsoleView():
    def  __init__(self):
        self.menu = Menu()
        self.work = True

    def start_application(self):
        print("Заметки")
        print("Нажмите 'q' для выхода")
        while(self.work):
            self.menu.print_main_menu()
            command = input("Введите номер команды: ")
            if command == 'q':
                self.finish()
                break
            number = int(command)
            self.menu.execute(number)

    def finish(self):
        print("Выход")
        self.work = False



            

        
            

