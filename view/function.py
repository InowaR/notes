from presenter.presenter import Presenter

class Function():
    def __init__(self):
        self.presenter = Presenter()

    def create_note(self):
        self.presenter.create_note()

    def show_notes(self):
        self.presenter.show_all_notes()

    def find_note_by_id(self):
        self.presenter.find_note_by_id()