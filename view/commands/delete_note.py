class DeleteNote():
    def __init__(self, presenter):
        self.name = "Удалить заметку"
        self.presenter = presenter
    
    def get_name(self):
        return self.name
    
    def execute(self):
        self.presenter.delete_note()