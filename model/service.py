import datetime
from model.list_notes import ListNotes
from model.note import Note

class Service():
    def __init__(self):
        self.id = 0
        self.date = datetime.datetime.today()
        self.notes = ListNotes()

    def create_note(self, title, body):
        note = Note(self.id, title, body, self.date)
        print(note)
        print(note.get_id())
        self.notes.add_note(note)
        self.id += 1

    def show_all_notes(self):
        print(self.notes.show_all_notes())

    def find_note_by_id(self, id):
        self.notes.find_note_by_id(id)