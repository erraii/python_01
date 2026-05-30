#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_ = age
        # self.show()

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age_} days old")
        # message = self.name + ": "
        # message += str(round(self.height, 1)) + "cm, "
        # message += str(self.age) + " days old"
        # print(message)


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25.0, 30)
    print("Created:", end=" ")
    rose.show()
    oak = Plant("Oak", 200.0, 365)
    print("Created:", end=" ")
    oak.show()
    cactus = Plant("Cactus", 5.0, 90)
    print("Created:", end=" ")
    cactus.show()
    sunflower = Plant("Sunflower", 80.0, 45)
    print("Created:", end=" ")
    sunflower.show()
    fern = Plant("Fern", 15.0, 120)
    print("Created:", end=" ")
    fern.show()
