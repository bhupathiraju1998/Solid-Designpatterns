# “Add new behavior to an object dynamically WITHOUT modifying the original class.”
from abc import ABC, abstractmethod


# -----------------------------
# Component Interface
# -----------------------------
class Coffee(ABC):

    # Why we wrote this line:
    # All coffee objects must provide cost() method.
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass


# -----------------------------
# Concrete Component
# -----------------------------
class SimpleCoffee(Coffee):

    # Why we wrote this line:
    # Base coffee price.
    def cost(self):
        return 5

    # Why we wrote this line:
    # Base coffee description.
    def description(self):
        return "Simple Coffee"


# -----------------------------
# Base Decorator
# -----------------------------
class CoffeeDecorator(Coffee):

    # Why we wrote this line:
    # Decorator wraps another coffee object.
    def __init__(self, coffee):

        self.coffee = coffee

    # Why we wrote this line:
    # Delegate cost to wrapped object.
    def cost(self):
        return self.coffee.cost()

    # Why we wrote this line:
    # Delegate description to wrapped object.
    def description(self):
        return self.coffee.description()


# -----------------------------
# Concrete Decorators
# -----------------------------
class MilkDecorator(CoffeeDecorator):

    # Why we wrote this line:
    # Add milk cost on top of existing coffee.
    def cost(self):
        return self.coffee.cost() + 2

    # Why we wrote this line:
    # Extend description dynamically.
    def description(self):
        return self.coffee.description() + ", Milk"


class SugarDecorator(CoffeeDecorator):

    def cost(self):
        return self.coffee.cost() + 1

    def description(self):
        return self.coffee.description() + ", Sugar"


# -----------------------------
# Usage
# -----------------------------

# Base coffee
coffee = SimpleCoffee()

print(coffee.description())
print(coffee.cost())

print("-----")

# Add milk
coffee_with_milk = MilkDecorator(coffee)

print(coffee_with_milk.description())
print(coffee_with_milk.cost())

print("-----")

# Add sugar on top of milk coffee
special_coffee = SugarDecorator(coffee_with_milk)

print(special_coffee.description())
print(special_coffee.cost())