from view.function import Function

class ShowNotes(Function):
    def __init__(self):
        self.name = "Показать список заметок"
        super().__init__(self)
    
    def get_name(self):
        return self.name
    
    def execute():
        super().show_notes()