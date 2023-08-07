from view.function import Function

class CreateNote(Function):
    def __init__(self):
        self.name = "Добавить заметку"
        super().__init__(self)
    
    def get_name(self):
        return self.name
    
    def execute():
        super().create_note()