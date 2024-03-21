class MenuNote:
    def __init__(self, db_conn=None) -> None:
        self.db_conn = db_conn

    def showOptions(self) -> None:
        print("Options:")
        print("1 - List notes")
        print("2 - View note")
        print("3 - Add note")
        print("4 - Edit note")
        print("5 - Delete note")
        print("0 - Exit")
        return None

    def askChoice(self) -> int:
        choice = input("Your choice: ")
        return int(choice)

    def activate(self) -> None:
        while True:
            self.showOptions()
            choice = self.askChoice()

            if choice == 1:
                self.listNotes()
            elif choice == 2:
                self.viewNote()
            elif choice == 3:
                self.addNote()
            elif choice == 4:
                self.editNote()
            elif choice == 5:
                self.deleteNote()
            elif choice == 0:
                
                break
            else:
                print("Invalid choice. Please try again.")
        return None

    def listNotes(self) -> None:
        print("List notes to be implemented...\n")
       
        return None

    def viewNote(self) -> None:
        print("View note to be implemented...\n")
        return None

    def addNote(self) -> None:
        print("Add note to be implemented...\n")
        
        return None

    def editNote(self) -> None:
        print("Edit note to be implemented...\n")
       
        return None

    def deleteNote(self) -> None:
        print("Delete note to be implemented...\n")
       
        return None
