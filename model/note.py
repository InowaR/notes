import datetime

class Note():
    def __init__(self, id, title, body, date):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def __str__(self) -> str:
        return f'Заметка: {self.id}, Имя: {self.title}, Тело: {self.body}, Дата: {self.date.strftime("%Y-%m-%d %H.%M.%S")}'
    
    def set_id(self, id):
        self.id = id
    
    def get_id(self):
        return self.id
    
    def set_title(self, title):
        self.title = title
    
    def get_title(self):
        return self.title
    
    def set_body(self, body):
        self.body = body

    def get_body(self):
        return self.body
    
    def set_date(self):
        self.date = datetime.datetime.today()
    
    def get_date(self):
        return self.date