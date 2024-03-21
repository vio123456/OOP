from model_note import Note, NoteDAO



def test_get_notes() -> None:

    notes = NoteDAO.getNotes()
    for note in notes:
        print(repr(note))
    return None 

class Main:
    def __init__(self) -> None:
    
        test_get_notes()
        return None 

if __name__ == "__main__":
    app = Main()
