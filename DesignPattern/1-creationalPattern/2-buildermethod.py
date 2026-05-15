# Concept: The Builder pattern is a helper that lets you construct complex objects step by step, allowing the exact same construction process to produce different variations or representations of that object
# -----------------------------
# Product (the final object)
# -----------------------------
class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.olives = False

    def __str__(self):
        toppings = []
        if self.cheese: toppings.append("cheese")
        if self.pepperoni: toppings.append("pepperoni")
        if self.mushrooms: toppings.append("mushrooms")
        if self.olives: toppings.append("olives")

        return f"{self.size} Pizza with " + ", ".join(toppings if toppings else ["no toppings"])


# -----------------------------
# Builder
# -----------------------------
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def add_olives(self):
        self.pizza.olives = True
        return self

    def build(self):
        return self.pizza


# -----------------------------
# Director (optional but useful)
# -----------------------------
class PizzaDirector:
    @staticmethod
    def make_margherita():
        return (PizzaBuilder()
                .set_size("Medium")
                .add_cheese()
                .build())

    @staticmethod
    def make_supreme():
        return (PizzaBuilder()
                .set_size("Large")
                .add_cheese()
                .add_pepperoni()
                .add_mushrooms()
                .add_olives()
                .build())


# -----------------------------
# Usage
# -----------------------------

# Manual building (flexible)
pizza1 = (PizzaBuilder()
          .set_size("Small")
          .add_cheese()
          .add_pepperoni()
          .build())

print(pizza1)

# Using Director (predefined recipes)
pizza2 = PizzaDirector.make_supreme()
print(pizza2)