class EditNote():
    def __init__(self, presenter):
        self.name = "Изменить заметку"
        self.presenter = presenter
    
    def get_name(self):
        return self.name
    
    def execute(self):
        self.presenter.edit_note()