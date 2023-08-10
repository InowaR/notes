class Note():
    def __init__(self, id, title, body, date):
        self._id = id
        self._title = title
        self._body = body
        self._date = date

    def __str__(self) -> str:
        return f'Заметка: {self.id}, Имя: {self.title}, Тело: {self.body}, Дата: {self.date.strftime("%Y-%m-%d %H.%M.%S")}'
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title

    @property
    def body(self):
        return self._body
    
    @body.setter
    def body(self, body):
        self._body = body
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        self._date = date