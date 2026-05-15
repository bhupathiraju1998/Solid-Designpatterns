# Concept: High-level modules (your core business logic) should not depend on low-level modules (specific tools or details); both should depend entirely on abstractions (interfaces


# Why we wrote this line: We import ABC and abstractmethod to build our strict abstraction (the interface).
from abc import ABC, abstractmethod

# Why we wrote this line: We create a Switchable interface so high-level and low-level modules have a common rule to depend on.
class Switchable(ABC):
    
    # Why we wrote this line: We force any connectable device to define exactly how it turns on.
    @abstractmethod
    def turn_on(self) -> str:
        # Why we wrote this line: We leave it empty because the interface only dictates the rule, not the implementation.
        pass
        
    # Why we wrote this line: We force any connectable device to define exactly how it turns off.
    @abstractmethod
    def turn_off(self) -> str:
        # Why we wrote this line: We leave it empty as a placeholder.
        pass


# Why we wrote this line: We create a LightBulb class (a low-level detail) that inherits from the Switchable abstraction.
class LightBulb(Switchable):
    
    # Why we wrote this line: We provide the actual, specific logic for turning on a light bulb.
    def turn_on(self) -> str:
        # Why we wrote this line: We return a string simulating the light turning on.
        return "LightBulb: Shining bright!"
        
    # Why we wrote this line: We provide the actual logic for turning off the light bulb.
    def turn_off(self) -> str:
        # Why we wrote this line: We return a string simulating the light turning off.
        return "LightBulb: Going dark."


# Why we wrote this line: We create a Fan class (another low-level detail) to prove we can easily add new devices.
class Fan(Switchable):
    
    # Why we wrote this line: We implement the specific logic for turning on a fan.
    def turn_on(self) -> str:
        # Why we wrote this line: We return a string simulating the fan spinning.
        return "Fan: Spinning up!"
        
    # Why we wrote this line: We implement the specific logic for turning off a fan.
    def turn_off(self) -> str:
        # Why we wrote this line: We return a string simulating the fan stopping.
        return "Fan: Spinning down."


# Why we wrote this line: We create our main Switch class (high-level module) which holds our core operational logic.
class Switch:
    
    # Why we wrote this line: We inject the dependency via the constructor, asking ONLY for the 'Switchable' interface, not a specific device!
    def __init__(self, device: Switchable):
        # Why we wrote this line: We store the injected device securely in a private variable.
        self.__device = device
        # Why we wrote this line: We create a private variable to track whether the switch is currently flipped up or down.
        self.__is_on = False

    # Why we wrote this line: We define a public method to let the outside world operate the switch.
    def press(self) -> str:
        # Why we wrote this line: We toggle the internal state of the switch from True to False, or False to True.
        self.__is_on = not self.__is_on
        
        # Why we wrote this line: We confidently use the abstraction's methods, completely blind to whether it is a Fan or a LightBulb.
        if self.__is_on:
            return self.__device.turn_on()
        return self.__device.turn_off()
    


# Why we wrote this line: We instantiate our low-level LightBulb object first.
my_bulb = LightBulb()

# Why we wrote this line: We pass the LightBulb into the Switch (This action is called "Dependency Injection"!).
living_room_switch = Switch(device=my_bulb)

# Why we wrote this line: We press the switch, which delegates the action to the bulb.
print(living_room_switch.press()) 
# Output: LightBulb: Shining bright!

# Why we wrote this line: We instantiate a completely different low-level device, a Fan.
my_fan = Fan()

# Why we wrote this line: We inject the Fan into a NEW Switch. The Switch class accepts it perfectly because it follows the contract.
bedroom_switch = Switch(device=my_fan)

# Why we wrote this line: We press the new switch, which flawlessly operates the fan.
print(bedroom_switch.press()) 
# Output: Fan: Spinning up!