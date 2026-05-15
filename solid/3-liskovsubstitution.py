# LSP prevents you from creating child classes that lie about what they can do
# parent bankaccount with calss withdraw child fixedaccount bu user cannot withdraw from fixed account
#  You never force a child class to inherit a behavior it cannot perform. Instead of making FixedDepositAccount inherit from Account, you separate them or use smaller, more specific abstract classes
# -->another example is birds parent class we degine methods that applies to all birds like eat but not fly method 
# becausse pengin cnaot fly so we write seperate class for fly and pass the bird class as parent so now sparrow  will ahve access to both flying class ad bird class 
# there is a new issue we are tightly coupling the inheritance with each class but m=we must do composition here like we split the behaviousrs like each class for a behaviour eat class , fly class ... etc adn we the main bird class will have a any of the behaviousr passed while object creations of bird


# Topic 3: Liskov Substitution Principle (LSP)
# Concept: A child class must be able to replace its parent class without breaking the application or changing the expected behavior
# Why we wrote this line: We import the ABC module to create an abstract base class that sets the contract.
from abc import ABC, abstractmethod

# Why we wrote this line: We create a general Bird class for properties that ALL birds share (like having a name).
class Bird(ABC):
    
    # Why we wrote this line: We initialize the Bird with a name to keep its data encapsulated.
    def __init__(self, name: str):
        # Why we wrote this line: We set the name as a private variable to protect the data from outside interference.
        self.__name = name

    # Why we wrote this line: We provide a public method so the outside world can safely read the bird's private name.
    def get_name(self) -> str:
        # Why we wrote this line: We return the private name variable.
        return self.__name

# Why we wrote this line: We create a SEPARATE interface strictly for flying behavior, because not all birds fly!
class FlyingBird(Bird):
    
    # Why we wrote this line: We use abstractmethod to FORCE any flying bird to implement exactly how it flies.
    @abstractmethod
    # Why we wrote this line: We define the fly method signature to ensure consistent usage across all flying birds.
    def fly(self) -> str:
        # Why we wrote this line: We pass because the specific bird must provide the actual flying implementation.
        pass

# Why we wrote this line: We create an Eagle class that inherits from FlyingBird because an Eagle CAN fly (this strictly follows LSP).
class Eagle(FlyingBird):
    
    # Why we wrote this line: We override the abstract fly method with the Eagle's specific flight behavior.
    def fly(self) -> str:
        # Why we wrote this line: We return a string confirming the eagle is flying, satisfying the contract.
        return f"{self.get_name()} is soaring high!"

# Why we wrote this line: We create a Penguin class that inherits ONLY from Bird, NOT FlyingBird, because penguins cannot fly.
class Penguin(Bird):
    
    # Why we wrote this line: We provide a swimming method because that is what penguins actually do, avoiding a broken fly() method.
    def swim(self) -> str:
        # Why we wrote this line: We return a string confirming the penguin is swimming.
        return f"{self.get_name()} is swimming fast!"


# Why we wrote this line: We create a main function that ONLY accepts birds that belong to the FlyingBird category.
def make_birds_fly(birds: list[FlyingBird]):
    # Why we wrote this line: We loop through the list of flying birds to trigger their behavior.
    for bird in birds:
        # Why we wrote this line: We confidently call fly(), knowing LSP guarantees every object here has a perfectly working fly method.
        print(bird.fly())


# Why we wrote this line: We instantiate (create) an Eagle object named "Apollo" so we have a real flying bird to work with.
my_eagle = Eagle("Apollo")

# Why we wrote this line: We instantiate a Penguin object named "Pingu" so we have a real non-flying bird in our system.
my_penguin = Penguin("Pingu")

# Why we wrote this line: We create a list specifically to hold flying birds, and we ONLY put the eagle inside it.
flock_of_flyers = [my_eagle]

# Why we wrote this line: We pass our safe list into the function, knowing absolutely every bird inside is guaranteed to know how to fly.
make_birds_fly(flock_of_flyers)

# Why we wrote this line: We handle the penguin completely separately by calling its unique swim method, respecting its specific abilities.
print(my_penguin.swim())