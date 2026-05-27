#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_ = age
        print("Created:", end=" ")
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age_} days old")
        # message = self.name + ": "
        # message += str(round(self.height, 1)) + "cm, "
        # message += str(self.age) + " days old"
        # print(message)


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)
