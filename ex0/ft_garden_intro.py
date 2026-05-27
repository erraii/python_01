#!/usr/bin/env python3

def ft_garden_intro(plant: str, height: int, age: int) -> None:
    print("=== Welcome to My Garden ===")
    print("Plant: " + plant)
    print("Height: " + str(height) + "cm")
    print("Age: " + str(age) + " days\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    plant = "Rose"
    height = 25
    age = 30
    ft_garden_intro(plant, height, age)
