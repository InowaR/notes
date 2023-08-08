class ShowNotes():
    def __init__(self, presenter):
        self.name = "Показать список заметок"
        self.presenter = presenter
    
    def get_name(self):
        return self.name
    
    def execute(self):
        self.presenter.show_all_notes()