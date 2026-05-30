#!/usr/bin/env python3

class Plant:

    class Statsdata:
        # stats for the class

        def __init__(self, plant: "Plant") -> None:
            self._plant = plant
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def count_grow(self) -> None:
            self._grow_count += 1

        def count_age(self) -> None:
            self._age_count += 1

        def count_show(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print(f"[statistics for {self._plant.name}]")
            msg = f"Stats: {self._grow_count} grow, {self._age_count} age, "
            msg += f"{self._show_count} show"
            print(msg)

    # def create_stats(self) -> Statsdata:
    #    return self.Statsdata(self)

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age_ = age
        # self._stats = self.create_stats()
        self._stats = self.Statsdata(self)

    def show(self) -> None:
        self._stats.count_show()
        message = f"{self.name}: {round(self._height, 1)}cm"
        message += f", {self._age_} days old"
        print(message)

    def grow(self, height: float) -> None:
        self._stats.count_grow()
        self._height += height

    def age(self, age: int) -> None:
        self._stats.count_age()
        self._age_ += age

    @staticmethod
    def check_year(days: int) -> None:
        print(f"Is {days} days more than a year? -> {days > 365}")

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        self._color = color
        self._bloom_ = False
        super().__init__(name, height, age)

    def bloom(self) -> None:
        # print(f"[asking the {self.name.lower()} to bloom]")
        self._bloom_ = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._bloom_:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str, bloom_seeds: int) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0
        self._bloom_seeds = bloom_seeds
        self._bloom_ = False

    def show(self) -> None:
        super().show()
        if self._bloom_:
            self._seeds = self._bloom_seeds
        print(f" Seeds: {self._seeds}")


class Tree(Plant):

    class Treestatsdata(Plant.Statsdata):
        def __init__(self, plant: "Plant") -> None:
            self._shade_count = 0
            super().__init__(plant)

        def count_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_count} shade")

    # def create_stats(self) -> Treestatsdata:
    #    return self.Treestatsdata(self)

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._stats = self.Treestatsdata(self)
        self._trunk_diameter = trunk_diameter
        # self._treestats = self.create_stats()

    def produce_shade(self) -> None:
        if isinstance(self._stats, self.Treestatsdata):
            self._stats.count_shade()
        print(f"[asking the {self.name.lower()} to produce shade]")
        msg = f"Tree {self.name} now produces a shade of {self._height}"
        msg += f"cm long and {self._trunk_diameter}cm wide"
        print(msg)

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


"""
class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        print("=== Vegetable")
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value
        super().__init__(name, height, age)

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def age_veg(self) -> None:
        super().age(1)

    def grow_veg(self) -> None:
        super().grow(1.0)
        self._nutritional_value += 1
"""


def show_stats(plant: Plant) -> None:
    plant._stats.display()
    # if isinstance(plant, Tree):
    #    print(f" {plant._treestats._shade_count} shade")


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_year(30)
    Plant.check_year(400)
    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    show_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    show_stats(rose)
    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    show_stats(oak)
    oak.produce_shade()
    show_stats(oak)
    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 42)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    show_stats(sunflower)
    print("\n=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    show_stats(anonymous)
    # tomato = Vegetable("Tomato", 5.0, 10, 2.1, "April", 0)
    # tomato.age_and_grow(20)
    # tomato.show()
