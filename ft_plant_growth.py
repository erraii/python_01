#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth: float) -> None:
        self.name = name
        self.height = height
        self.age_ = age
        self.growth = growth

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age_} days old")
        # message = self.name + ": "
        # message += str(round(self.height, 1)) + "cm, "
        # message += str(self.age) + " days old"
        # print(message)

    def grow(self) -> None:
        self.height += self.growth

    def age(self) -> None:
        self.age_ += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30, 0.8)
    # sunflower = Plant("Sunflower", 80.0, 15, 1.8)
    # cactus = Plant("Cactus", 15.0, 120, 0.1)
    total_growth = 0.0

    for i in range(1, 8):
        print("=== Day " + str(i) + " ===")
        rose.show()
        rose.grow()
        total_growth += rose.growth
        rose.age()
        # sunflower.show()
        # sunflower.grow()
        # total_growth += sunflower.growth
        # sunflower.age()
        # cactus.show()
        # cactus.grow()
        # total_growth += cactus.growth
        # cactus.age()
    print("Growth this week: " + str(round(total_growth)) + "cm")
