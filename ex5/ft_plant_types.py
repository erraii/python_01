#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth: float) -> None:
        self.name = name
        self._height = height
        self._age_ = age
        self._growth = growth
        # print("Plant Created:", end=" ")

    def show(self) -> None:
        message = f"{self.name}: {round(self._height, 1)}cm"
        message += f", {self._age_} days old"
        print(message)

    def grow(self) -> None:
        self._height += self._growth

    def age(self) -> None:
        self._age_ += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, growth: float,
                 color: str) -> None:
        super().__init__(name, height, age, growth)
        self._color = color
        self._bloom_ = False

    def bloom(self) -> None:
        print(f"[asking the {self.name.lower()} to bloom]")
        self._bloom_ = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._bloom_:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, growth: float,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age, growth)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self.name.lower()} to produce shade]")
        msg = f"Tree {self.name} now produces a shade of {self._height}"
        msg += f"cm long and {self._trunk_diameter}cm wide."
        print(msg)

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, growth: float,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age, growth)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def age(self) -> None:
        super().age()

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 0.8, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print("")
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 0.2, 5.0)
    oak.show()
    oak.produce_shade()
    print("")
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, 2.1, "April", 0)
    tomato.show()
    days = 20
    print(f"[make {tomato.name.lower()} grow and age for {days} days]")
    for i in range(days):
        tomato.age()
        tomato.grow()
    tomato.show()
