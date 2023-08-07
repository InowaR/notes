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
