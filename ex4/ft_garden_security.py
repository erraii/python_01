#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            self._height = 0.0
        else:
            self._height = height
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            self._age = 0
        else:
            self._age = age
        print("Plant created:", end=" ")
        self.show()

    def show(self) -> None:
        message = f"{self.name}: {round(self.get_height(), 1)}cm"
        message += f", {self.get_age()} days old"
        print(message)

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {round(self.get_height(), 1)}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self.get_age()} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("")
    # oak = Plant("Oak", 200.0, 365)
    # cactus = Plant("Cactus", 5.0, 90)
    # sunflower = Plant("Sunflower", 80.0, 45)
    # fern = Plant("Fern", 15.0, 120)
    rose.set_height(25.0)
    rose.set_age(30)
    print("")
    rose.set_height(-10)
    rose.set_age(-1)
    print("\nCurrent state:", end=" ")
    rose.show()
