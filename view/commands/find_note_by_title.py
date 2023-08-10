class FindNoteByTitle():
    def __init__(self, presenter):
        self.name = "Найти заметку по названию"
        self.presenter = presenter

    def get_name(self):
        return self.name
    
    def execute(self):
        self.presenter.find_note_by_title()