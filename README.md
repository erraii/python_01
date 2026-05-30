# Python Module 01 - Garden OOP Project

This repository contains my solutions for the Python Module 01 project.

The project is organized as a set of small exercises that gradually introduce Python program structure and Object-Oriented Programming concepts. Each exercise focuses on a specific topic such as variables, classes, methods, initialization, encapsulation, inheritance, and advanced OOP features.

## Repository Structure

```text
python_01/
├── ex0/
│   └── ft_garden_intro.py
├── ex1/
│   └── ft_garden_data.py
├── ex2/
│   └── ft_plant_growth.py
├── ex3/
│   └── ft_plant_factory.py
├── ex4/
│   └── ft_garden_security.py
├── ex5/
│   └── ft_plant_types.py
├── ex6/
│   └── ft_garden_analytics.py
└── README.md
```

## Requirements

- Python 3.10 or higher
- Code compatible with `flake8`
- Type hints for functions and methods
- No external Python packages are required

## How to Run

Each exercise can be executed separately from the root of the repository.

```bash
python3 ex0/ft_garden_intro.py
python3 ex1/ft_garden_data.py
python3 ex2/ft_plant_growth.py
python3 ex3/ft_plant_factory.py
python3 ex4/ft_garden_security.py
python3 ex5/ft_plant_types.py
python3 ex6/ft_garden_analytics.py
```

You can also run files directly if they have execution permission and a shebang line:

```bash
chmod +x ex0/ft_garden_intro.py
./ex0/ft_garden_intro.py
```

## Exercises

### Exercise 0 - Planting Your First Seed

File:

```text
ex0/ft_garden_intro.py
```

This exercise introduces the basic structure of a Python program.

Main concepts:

- Simple variables
- Printing output
- Program entry point
- `if __name__ == "__main__"` pattern

The program stores basic plant information such as name, height, and age, then displays the information using `print()`.

The `if __name__ == "__main__"` block makes sure the main code runs only when the file is executed directly, not when it is imported by another Python file.

### Exercise 1 - Garden Data Organizer

File:

```text
ex1/ft_garden_data.py
```

This exercise introduces classes as a way to organize related data.

Main concepts:

- Class definition
- Object creation
- Instance attributes
- Displaying object data

A `Plant` class is used to group plant-related information inside objects. Instead of storing plant data in separate variables, each plant is represented as an instance of the class.

### Exercise 2 - Plant Growth Simulator

File:

```text
ex2/ft_plant_growth.py
```

This exercise introduces methods.

Main concepts:

- Methods inside classes
- Calling methods on objects
- Changing object state
- Simulating plant growth over time

Plants can grow and age through method calls. The state of each plant object changes persistently when methods are executed.

### Exercise 3 - Plant Factory

File:

```text
ex3/ft_plant_factory.py
```

This exercise introduces object initialization with `__init__`.

Main concepts:

- Constructor method
- Initial object state
- Passing parameters during object creation
- Creating multiple objects with different values

The `__init__` method is used to initialize plant objects with starting values such as name, height, and age.

### Exercise 4 - Garden Security System

File:

```text
ex4/ft_garden_security.py
```

This exercise introduces encapsulation.

Main concepts:

- Protected attributes using the single underscore convention
- Getter methods
- Setter methods
- Data validation
- Rejecting invalid values

Plant data is protected by using internal attributes such as `_height` and `_age`. Values are updated through setter methods, which check whether the new values are valid before modifying the object.

For example, negative height or age values are rejected to keep the plant data consistent.

### Exercise 5 - Specialized Plant Types

File:

```text
ex5/ft_plant_types.py
```

This exercise introduces inheritance.

Main concepts:

- Parent class
- Child classes
- Code reuse
- `super()`
- Method overriding

A general `Plant` class contains common plant behavior. Specialized classes such as `Flower`, `Tree`, and `Vegetable` inherit from the base class and add their own specific features.

Inheritance allows shared functionality to be reused while still allowing each plant type to have unique behavior.

### Exercise 6 - Garden Analytics Platform

File:

```text
ex6/ft_garden_analytics.py
```

This exercise demonstrates more advanced Object-Oriented Programming concepts.

Main concepts:

- Nested classes
- Inheritance chains
- Static methods
- Class methods
- Instance methods
- Non-member functions
- Method overriding

The program includes a statistics system related to plant objects. A nested class is used to store and display statistics. The exercise also demonstrates the difference between methods that belong to a class and standalone functions outside a class.

A non-member function receives a plant object as a parameter and uses the plant's public behavior to display statistics.

## OOP Concepts Covered

### Class

A class is a blueprint for creating objects.

Example:

```python
class Plant:
    pass
```

### Instance / Object

An instance is an object created from a class.

Example:

```python
rose = Plant()
```

Here, `rose` is an instance of the `Plant` class.

### Method

A method is a function defined inside a class.

Example:

```python
def grow(self) -> None:
    self.height += 1
```

### `self`

`self` represents the current object.

When calling:

```python
rose.grow()
```

`self` refers to `rose`.

When calling:

```python
cactus.grow()
```

`self` refers to `cactus`.

This allows the same method to work on different objects.

### `__init__`

`__init__` is the constructor method. It runs automatically when a new object is created.

Example:

```python
def __init__(self, name: str, height: int) -> None:
    self.name = name
    self.height = height
```

### Encapsulation

Encapsulation means controlling access to object data.

In Python, a single underscore is used by convention:

```python
self._height = height
```

This means the attribute is intended for internal use. It should be modified through methods such as setters.

### Inheritance

Inheritance allows one class to reuse code from another class.

Example:

```python
class Tree(Plant):
    pass
```

Here, `Tree` inherits from `Plant`.

### `super()`

`super()` is used to call a method from the parent class.

Example:

```python
super().show()
```

This allows a child class to reuse parent behavior and extend it.

### Static Method

A static method belongs to a class logically, but it does not need access to the object or the class itself.

It does not use `self` or `cls`.

### Class Method

A class method receives the class as its first parameter, usually named `cls`.

It can be used to create objects or work with class-level behavior.

### Non-Member Function

A non-member function is a normal function outside any class.

Example:

```python
def show_stats(plant: Plant) -> None:
    plant.show()
```

It does not belong to the class, but it can receive an object as a parameter.

## Code Quality Checks

The project can be checked with:

```bash
python3 -m py_compile ex0/ft_garden_intro.py ex1/ft_garden_data.py ex2/ft_plant_growth.py ex3/ft_plant_factory.py ex4/ft_garden_security.py ex5/ft_plant_types.py ex6/ft_garden_analytics.py
```

Optional checks:

```bash
flake8 ex0 ex1 ex2 ex3 ex4 ex5 ex6
mypy ex0 ex1 ex2 ex3 ex4 ex5 ex6
```

## Project Goal

The goal of this project is to practice Python basics and Object-Oriented Programming step by step.

The exercises start with simple variables and program structure, then gradually move toward classes, methods, constructors, encapsulation, inheritance, and advanced OOP concepts.
