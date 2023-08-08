from presenter.presenter import Presenter
from view.commands.exit import Exit
from view.commands.find_note_by_id import FindNoteById
from view.commands.create_note import CreateNote
from view.commands.show_notes import ShowNotes

class Menu():
    def __init__(self):
        self.presenter = Presenter()
        self.commands_main_menu = []
        self.commands_main_menu.append(ShowNotes(self.presenter))
        self.commands_main_menu.append(CreateNote(self.presenter))
        self.commands_main_menu.append(FindNoteById(self.presenter))
        self.commands_main_menu.append(Exit())

    def print_main_menu(self):
        print("Меню:")
        for i in self.commands_main_menu:
            print(f'{self.commands_main_menu.index(i)}. {i.get_name()}')

    def execute(self, number):
        self.commands_main_menu[number].execute()