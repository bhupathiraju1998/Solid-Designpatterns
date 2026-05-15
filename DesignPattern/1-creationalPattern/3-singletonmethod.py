# Concept: The Singleton pattern ensures that a class has only one instance and provides a global access point to it liek the database intialization
# only one object of this class should ever exist in the entire application
# -----------------------------
# Singleton Class
# -----------------------------
class DatabaseConnection:

    # Why we wrote this line:
    # We store the ONE shared instance here.
    _instance = None

    # Why we wrote this line:
    # __new__ controls object creation BEFORE __init__ runs.
    def __new__(cls):

        # Why we wrote this line:
        # If no object exists yet, create it once.
        if cls._instance is None:

            print("Creating new database connection...")

            # Why we wrote this line:
            # super().__new__(cls) actually allocates memory for the object.
            cls._instance = super().__new__(cls)

        # Why we wrote this line:
        # Return the SAME object every time.
        return cls._instance

    # Why we wrote this line:
    # Normal initialization logic.
    def __init__(self):
        self.connection = "Connected to database"

    # Why we wrote this line:
    # Human-readable string output.
    def __str__(self):
        return self.connection


# -----------------------------
# Usage
# -----------------------------

db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1)
print(db2)

# Why we wrote this line:
# 'is' checks if both variables point to the SAME memory object.
print(db1 is db2)