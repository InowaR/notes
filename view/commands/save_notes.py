class SaveNotes():
    def __init__(self, presenter):
        self.name = "Сохранить заметки в файл"
        self.presenter = presenter
    
    def get_name(self):
        return self.name
    
    def execute(self):
        self.presenter.save_notes()