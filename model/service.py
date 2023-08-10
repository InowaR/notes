import datetime
from model.list_notes import ListNotes
from model.note import Note

class Service():
    def __init__(self):
        self.id = 0
        self.date = datetime.datetime.today()
        self.notes = ListNotes()

    def get_length(self):
        return len(self.notes.get_list_notes())

    def set_id(self, id):
        self.id = id

    def create_note(self, title, body):
        note = Note(self.id, title, body, self.date)
        print(note)
        print(note.id)
        self.notes.add_note(note)
        self.id += 1

    def show_all_notes(self):
        print(self.notes.show_all_notes())

    def find_note_by_id(self, id):
        self.notes.find_note_by_id(id)

    def save_notes(self):
        self.notes.save_notes()

    def load_notes(self):
        self.notes.load_notes()

    def edit_note(self, id, title, body):
        self.notes.edit_note(id, title, body)

    def delete_note(self, id):
        self.notes.delete_note(id)
        self.id -= 1