from view.menu import Menu


class ConsoleView():
    def  __init__(self) -> None:
        self.work = True

    def start_application(self, work):
        while(work):
            menu = Menu()
            menu.print_menu()

    def execute_command():
        command = int(input("Введите номер команды: "))
        
            

