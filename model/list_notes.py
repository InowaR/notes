import csv
import datetime
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
            if note.get_id() == id:
                print("Заметка найдена")
                print(note)

    def save_notes(self):
        filename = 'notes.csv'
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body', 'date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for note in self.list_notes:
                writer.writerow({'id': note.get_id(), 'title': note.get_title(), 'body': note.get_body(), 'date': note.get_date().strftime('%Y-%m-%d %H:%M:%S')})
        print("Заметка сохранена")

    def load_notes(self):
        filename = 'notes.csv'
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                id = int(row['id'])
                title = row['title']
                body = row['body']
                date = datetime.datetime.strptime(row['date'], '%Y-%m-%d %H:%M:%S')
                self.list_notes.append(Note(id, title, body, date))
        print("Заметка загружена")

    def edit_note(self, id, title, body):
        for note in self.list_notes:
            if note.get_id() == id:
                note.set_title(title)
                note.set_body(body)
                note.set_date()

    def delete_note(self, id):
        for note in self.list_notes:
            if note.get_id() == id:
                self.list_notes.remove(note)



        