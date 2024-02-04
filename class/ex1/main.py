from car import Car

class Main:
    def __init__(self):
        print("Program starting")
        # 1. Initiate 
        car1 = Car("red")
        car2 = Car("blue")
        # 2. Operate
        car1.start()
        car2.start()
        print(f"Car1 speed {car1.speed}")
        car1.accelerate(10.0)
        print(f"Car1 speed {car1.speed}")
        # 3. Terminate
        print("Program ending.")
        return None
if __name__ == "__main__":
    app = Main()