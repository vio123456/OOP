import sqlite3
import sys

class DB_CONN:
    @staticmethod
    def loadSqlScript(filepath: str) -> str:
        try:
            with open(filepath, 'r', encoding='UTF-8') as file:
                return file.read()
        except Exception as e:
            print(f"Failed to read '{filepath}' file.")
            sys.exit(-1)

    @staticmethod
    def initializeDB() -> None:
        script = DB_CONN.loadSqlScript("setup.sql")
        conn = sqlite3.connect("notes.db")
        cursor = conn.cursor()
        cursor.executescript(script)
        conn.commit()
        cursor.close()
        return None
