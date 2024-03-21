from db_conn import DB_CONN
from menu_note import MenuNote

class Main:
    def __init__(self) -> None:
        # Initialize the database
        DB_CONN.initializeDB()
        # Start the menu interface
        self.menu = MenuNote()
        self.menu.activate()
        return None

if __name__ == "__main__":
    app = Main()
