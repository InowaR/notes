from view.function import Function

class FindNoteById(Function):
    def __init__(self):
        self.name = "Найти заметку"
        super().__init__(self)

    def get_name(self):
        return self.name
    
    def execute():
        super().find_note_by_id()