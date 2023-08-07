class ListNotes():
    def __init__(self):
        self.list_notes = []

    def add_note(self, note):
        self.list_notes.append(note)

    def show_all_notes(self):
        for note in self.list_notes:
            print(note)
