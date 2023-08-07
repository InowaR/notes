class Note():
    def __init__(self, id, title, body, date):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def __str__(self) -> str:
        return f'Заметка: {self.id}, Имя: {self.title}, Тело: {self.body}, Дата: {self.date.strftime("%Y-%m-%d-%H.%M.%S")}'
    
    def get_id(self):
        return self.id