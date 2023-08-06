class ListNotes():
    def __init__(self) -> None:
        self.list_notes = []

    def add_note(self, Note):
        self.list_notes.append(Note)