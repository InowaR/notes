import datetime

class Note():
    def __init__(self, id, title, body) -> None:
        self.id = id
        self.title = title
        self.body = body
        self.date = datetime.datetime.today()

    def __str__(self) -> str:
        return f'{self.id}, {self.title}, {self.body}, {self.date.strftime("%Y-%m-%d-%H.%M.%S")}'