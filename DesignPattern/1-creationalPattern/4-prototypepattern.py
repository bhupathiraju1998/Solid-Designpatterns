# Instead of creating a brand-new object from scratch, clone an existing object.”
import copy


# -----------------------------
# Prototype Class
# -----------------------------
class Character:

    # Why we wrote this line:
    # We initialize a complex object with many attributes.
    def __init__(self, name, weapon, armor, level):

        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.level = level

    # Why we wrote this line:
    # clone() creates a duplicate of the current object.
    def clone(self):

        # Why we wrote this line:
        # deepcopy creates a completely independent copy.
        return copy.deepcopy(self)

    # Why we wrote this line:
    # Human-readable output.
    def __str__(self):
        return (
            f"Character(name={self.name}, "
            f"weapon={self.weapon}, "
            f"armor={self.armor}, "
            f"level={self.level})"
        )


# -----------------------------
# Create Original Object
# -----------------------------

# Why we wrote this line:
# We create one fully configured prototype object.
warrior = Character(
    name="Warrior",
    weapon="Sword",
    armor="Steel Armor",
    level=10
)

print(warrior)


# -----------------------------
# Clone Existing Object
# -----------------------------

# Why we wrote this line:
# Instead of rebuilding from scratch, we clone the warrior.
warrior_clone = warrior.clone()

# Why we wrote this line:
# We customize only the fields we want changed.
warrior_clone.name = "Elite Warrior"
warrior_clone.level = 20

print(warrior_clone)