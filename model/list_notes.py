import csv
from datetime import datetime
from model.note import Note

class ListNotes():
    def __init__(self):
        self.list_notes = []

    def get_list_notes(self):
        return self.list_notes

    def add_note(self, note):
        self.list_notes.append(note)

    def show_all_notes(self):
        for note in self.list_notes:
            print(note)
    
    def find_note_by_id(self, id):
        for note in self.list_notes:
            if note.id == id:
                print("Заметка найдена")
                print(note)

    def find_note_by_title(self, title):
        for note in self.list_notes:
            if note.title == title:
                print("Заметка найдена")
                print(note)

    def save_notes(self):
        filename = 'notes.csv'
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body', 'date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for note in self.list_notes:
                writer.writerow({'id': note.id, 'title': note.title, 'body': note.body, 'date': note.date.strftime('%Y-%m-%d %H:%M:%S')})
        print("Заметки сохранены")

    def load_notes(self):
        filename = 'notes.csv'
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                id = int(row['id'])
                title = row['title']
                body = row['body']
                date = datetime.strptime(row['date'], '%Y-%m-%d %H:%M:%S')
                self.list_notes.append(Note(id, title, body, date))
        print("Заметки загружены")

    def edit_note(self, id, title, body, date):
        for note in self.list_notes:
            if note.id == id:
                note.title = title
                note.body = body
                note.date = date
        print("Заметка изменена")

    def delete_note(self, id):
        for note in self.list_notes:
            if note.id == id:
                self.list_notes.remove(note)
        print("Заметка удалена")

    def update_id(self):
        id = 0
        for note in self.list_notes:
            note.id = id
            id += 1


        