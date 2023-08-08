class CreateNote():
    def __init__(self, presenter):
        self.name = "Добавить заметку"
        self.presenter = presenter
    
    def get_name(self):
        return self.name
    
    def execute(self):
        self.presenter.create_note()
