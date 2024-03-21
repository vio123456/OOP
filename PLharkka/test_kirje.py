from kirje import Kirje, KirjeDetails

def display_mock_list() -> None:
    print("Show mock List of messages in streamlined style:")
    mock_list_details = KirjeDetails(
        content="1 - example\n2 - tomorrow",
        header_separation=" - ",
        headers={
            'ID': 'Title',
            'Title': ' notes '
        }
    )
    mock_list = Kirje(mock_list_details)
    mock_list.display("streamlined")

def display_mock_note() -> None:
    print("\nShow mock note in default style:")
    mock_note_details = KirjeDetails(
        content="eat\nstudy\nsleep",
        header_separation=" - ",
        headers={
            'ID': '2',
            'Title': 'tomorrow'
        }
    )
    mock_note = Kirje(mock_note_details)
    mock_note.display("default")

class Main:
    def __init__(self) -> None:
        display_mock_list()
        display_mock_note()

if __name__ == "__main__":
    app = Main()
