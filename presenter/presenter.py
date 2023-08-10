from model.service import Service

class Presenter():
    def __init__(self):
        self.service = Service()

    def create_note(self):
        title = input("Введите название заметки:\n")
        body = input("Введите тело заметки:\n")
        self.service.create_note(title, body)

    def show_all_notes(self):
        self.service.show_all_notes()

    def find_note_by_id(self):
        id = int(input("Введите номер ID: "))
        self.service.find_note_by_id(id)

    def save_notes(self):
        self.service.save_notes()

    def load_notes(self):
        self.service.load_notes()
        id = self.service.get_length()
        self.service.set_id(id)

    def edit_note(self):
        id = int(input("Для редактирования введите ID заметки:\n"))
        title = input("Введите новое название заметки:\n")
        body = input ("Введите новое тело заметки:\n")
        self.service.edit_note(id, title, body)

    def delete_note(self):
        id = int(input("Для удаления введите ID заметки:\n"))
        self.service.delete_note(id)