from dataclasses import dataclass
import sqlite3

@dataclass
class Note:
    id: int
    title: str
    content: str

class NoteDAO:
    db_path = 'notes.db'  

    @staticmethod
    def addNote(title: str, content: str) -> None:
        try:
            connection = sqlite3.connect(NoteDAO.db_path)
            cursor = connection.cursor()
            
            #
            sql_statement = 'INSERT INTO note (title, content) VALUES (?, ?)'
            cursor.execute(sql_statement, (title, content))
            
            connection.commit()
        except sqlite3.IntegrityError as e:
            print("Error while inserting note.", e)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def getNotes(limit: int = -1) -> list[Note]:
        connection = sqlite3.connect(NoteDAO.db_path)
        cursor = connection.cursor()
        
        query = 'SELECT id, title, content FROM note'
        if limit > 0:
            query += f' LIMIT {limit}'
        cursor.execute(query)
        
        records = cursor.fetchall()
        notes = [Note(id=record[0], title=record[1], content=record[2]) for record in records]
        
        cursor.close()
        connection.close()
        return notes

if __name__ == "__main__":

    NoteDAO.addNote('Sample Title', 'Sample Content')
    notes = NoteDAO.getNotes()
    print(notes)
