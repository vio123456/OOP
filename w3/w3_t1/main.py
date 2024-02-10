from person import Person

class Main:
    def __init__(self) -> None:
        print("Program starting.")
        self.run()
        print("Program ending.")
        return None  # Explicitly returning None

    def run(self) -> None:
        print("Creating person...")
        # Using hardcoded values as specified
        person = Person("John", "Doe", 30)
        print("Person created.")
        
        # Printing person's details
        print(f"Name: {person.getFullname()}")
        print(f"Age: {person.getAge()}")
        
        print("Person has now birthday...")
        person.ageUp()
        print(f"New age: {person.getAge()}")
        return None  # Explicitly returning None

if __name__ == "__main__":
    app = Main()
