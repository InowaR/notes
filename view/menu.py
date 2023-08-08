from view.commands.find_note_menu.find_note_by_id import FindNoteById
from view.commands.find_note_menu.return_back_to_menu import ReturnBackToMenu
from view.commands.main_menu.create_note import CreateNote
from view.commands.main_menu.exit import Exit
from view.commands.main_menu.find_note import FindNote
from view.commands.main_menu.show_notes import ShowNotes

class Menu():
    def __init__(self):
        self.commands_main_menu = []
        self.commands_find_note_menu = []

    def add_commands_to_main_menu(self):
        self.commands_main_menu.append(FindNote())
        self.commands_main_menu.append(ShowNotes())
        self.commands_main_menu.append(CreateNote())
        self.commands_main_menu.append(Exit())

    def add_commands_to_find_note_menu(self):
        self.commands_find_note_menu.append(FindNoteById())
        self.commands_find_note_menu.append(ReturnBackToMenu())

    def print_main_menu(self):
        print("Меню:")
        for i in self.commands_main_menu:
            print(f'{self.commands_main_menu.index(i)}. {i.get_name()}')


    def print_find_note_menu(self):
        for i in self.commands_find_note_menu:
            print(f'{self.commands_find_note_menu.index(i)}. {i.get_name()}')