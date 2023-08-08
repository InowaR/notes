class LoadNotes():
    def __init__(self, presenter):
        self.name = "Загрузить заметку"
        self.presenter = presenter
    
    def get_name(self):
        return self.name
    
    def execute(self):
        self.presenter.load_notes()