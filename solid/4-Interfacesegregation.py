# Topic 4: Interface Segregation Principle (ISP)
# Concept: Clients should not be forced to depend on interfaces they do not use, meaning large, "fat" interfaces should be split into smaller, more specific ones
# Why we wrote this line: We import ABC and abstractmethod to build strict, small interfaces.
from abc import ABC, abstractmethod

# Why we wrote this line: We create a specific interface strictly for the ability to work, isolating this single behavior.
class Workable(ABC):
    
    # Why we wrote this line: We force any working object to implement the exact steps of working.
    @abstractmethod
    def work(self) -> str:
        # Why we wrote this line: We leave it empty as a placeholder contract.
        pass

# Why we wrote this line: We create a separate, specific interface strictly for the ability to eat, separating it from working.
class Eatable(ABC):
    
    # Why we wrote this line: We force any eating object to define exactly how it eats.
    @abstractmethod
    def eat(self) -> str:
        # Why we wrote this line: We leave it empty as a placeholder contract.
        pass

# Why we wrote this line: We create a Human class that inherits from BOTH interfaces because humans do both jobs.
class Human(Workable, Eatable):
    
    # Why we wrote this line: We provide the specific working logic for a human.
    def work(self) -> str:
        # Why we wrote this line: We return a string to simulate a human working.
        return "Human is writing code."

    # Why we wrote this line: We provide the specific eating logic for a human.
    def eat(self) -> str:
        # Why we wrote this line: We return a string to simulate a human eating.
        return "Human is eating a sandwich."

# Why we wrote this line: We create a Robot class that inherits ONLY from Workable, perfectly following ISP!
class Robot(Workable):
    
    # Why we wrote this line: We provide the specific working logic for a machine.
    def work(self) -> str:
        # Why we wrote this line: We return a string to simulate a robot working.
        return "Robot is assembling parts."
        
    # Why we DID NOT write an eat() method here: Because we segregated the interfaces, Robot isn't forced to inherit Eatable, keeping our code clean of useless methods!
# Practical Usage of Our ISP Classes
# Code Example (Object Creation & Execution): Here is how we use our granular objects in the main part of our application.
# Why we wrote this line: We instantiate (create) a Human object so we have a worker that needs food.
human_worker = Human()

# Why we wrote this line: We instantiate a Robot object so we have an automated worker.
robot_worker = Robot()

# Why we wrote this line: We safely call the work method on the human.
print(human_worker.work())

# Why we wrote this line: We safely call the eat method on the human.
print(human_worker.eat())

# Why we wrote this line: We call the work method on the robot to perform its only job.
print(robot_worker.work())

# Why we DO NOT write this line (robot_worker.eat()): 




# diff btw lsp and interafca segreagation 
# However, there is a very subtle but important difference in why we do it compared to the Bird example (LSP):
# LSP (The Bird Example) focuses on the Subclass: It asks, "If I create a child class, will it lie about what it can do?" We separated FlyingBird from Bird so that the Penguin class wouldn't be forced to inherit a fly() method that would crash the program if someone tried to use it
# .
# ISP (The Robot Example) focuses on the Interface: It asks, "Is this blueprint trying to do too many unrelated things?" We separated Workable and Eatable because forcing a Robot to depend on a giant, bloated Worker interface means the robot is forced to carry around an eat() method that it doesn't even need
# .