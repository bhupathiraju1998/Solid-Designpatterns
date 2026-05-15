# Topic 2: The Open/Closed Principle (OCP)
# Concept: A class should be open for extension (adding new features) but closed for modification (changing the existing, working code)

# Why we wrote this line: We import ABC and abstractmethod to enable the creation of strict interfaces in Python.
from abc import ABC, abstractmethod

# Why we wrote this line: We define an abstract interface to act as a contract that all future payment methods MUST follow.
class PaymentStrategy(ABC):
    
    # Why we wrote this line: We use the abstractmethod decorator to force any child class to implement this exact method.
    @abstractmethod
    # Why we wrote this line: We define the method signature showing it takes an amount and returns a string, but we leave it empty.
    def process_payment(self, amount: float) -> str:
        # Why we wrote this line: We use 'pass' because the interface only sets the rule; it does not contain the actual behavior.
        pass

# Why we wrote this line: We create a specific class for Credit Cards that inherits from the PaymentStrategy interface.
class CreditCardPayment(PaymentStrategy):
    
    # Why we wrote this line: We override the abstract method to provide the actual logic required to process a credit card.
    def process_payment(self, amount: float) -> str:
        # Why we wrote this line: We return a string simulating a successful credit card transaction.
        return f"Processed ${amount} using Credit Card."

# Why we wrote this line: We create a PayPal class to add a NEW feature WITHOUT modifying the CreditCard or PaymentStrategy classes (This is OCP!).
class PayPalPayment(PaymentStrategy):
    
    # Why we wrote this line: We override the abstract method to provide the specific steps required to process PayPal.
    def process_payment(self, amount: float) -> str:
        # Why we wrote this line: We return a string simulating a successful PayPal transaction.
        return f"Processed ${amount} using PayPal."

# Why we wrote this line: We create a main Checkout class separate from payments to handle shopping cart logic (keeping Single Responsibility intact).
# 

class Checkout:
    
    # Why we wrote this line: We initialize the checkout process by asking for a PaymentStrategy object (this is called Dependency Injection).
    def __init__(self, payment_method: PaymentStrategy):
        # Why we wrote this line: We store the payment method in a private variable to protect it from unexpected outside changes.
        self.__payment_method = payment_method

    # Why we wrote this line: We define a public method to let the outside world trigger the checkout process safely.
    def execute_checkout(self, amount: float) -> str:
        # Why we wrote this line: We delegate the actual payment processing to whatever strategy was passed in, remaining ignorant of how it actually works.
        return self.__payment_method.process_payment(amount)
    

# 1. Real World Usage: A customer chooses to pay with a Credit Card. 
# We create the specific credit card strategy.
cc_strategy = CreditCardPayment()

# 2. We inject that strategy into our main Checkout class.
# The Checkout class doesn't know it's a credit card, it just knows it's a valid 'PaymentStrategy'.
cart_one = Checkout(payment_method=cc_strategy)
print(cart_one.execute_checkout(150.00))

# 3. Real World Usage: Another customer chooses PayPal. 
# We simply pass in the new strategy. The Checkout class behaves perfectly without any modifications.
paypal_strategy = PayPalPayment()
cart_two = Checkout(payment_method=paypal_strategy)
print(cart_two.execute_checkout(75.50))
# ------>

# But Strategy Pattern Needs Something Called a “Context”

# Every strategy pattern has 3 parts:

# Role	            Your Code
# Strategy Interface	PaymentStrategy
# Concrete Strategies	CreditCardPayment, PayPalPayment
# Context          	Checkout

# ------>
# the thing is we we wrote directly cc_strategy as creditcard but user an send idffernt so need to be dynamic in tah case 
# Register pattern comes into picture what register pattern does is it will register dictonary intially on app load so if user sends pay payalk we get teh class of paypal dynamically and we also ued stategy pattern
# Why we wrote this line: We create a simple dictionary to act as our Registry, mapping text strings to actual Python classes.

payment_registry = {}

# Why we wrote this line: We assign the string "credit_card" as a key and the CreditCardPayment CLASS blueprint (no parenthesis) as the value.
payment_registry["credit_card"] = CreditCardPayment

# Why we wrote this line: We assign the string "paypal" as a key and the PayPalPayment CLASS blueprint as the value.
payment_registry["paypal"] = PayPalPayment

# Why we wrote this line: We simulate a real-world scenario where a user selects a payment method from a website dropdown menu.
user_input = "paypal" 

# Why we wrote this line: We dynamically fetch the class blueprint from the dictionary using the user's text input, completely avoiding if-statements.
DynamicStrategyClass = payment_registry.get(user_input)

# Why we wrote this line: We dynamically create the object instance by adding parenthesis () to the fetched class blueprint!
dynamic_strategy = DynamicStrategyClass()

# Why we wrote this line: We pass our dynamically created strategy into the Checkout class, completely unaware of which one it actually is.
cart = Checkout(payment_method=dynamic_strategy)

# Why we wrote this line: We execute the checkout process to prove our dynamic system works perfectly.
print(cart.execute_checkout(150.00))
# In the real world, you register your classes when the application starts up
# . Then, whenever a request comes in, the dictionary dynamically routes it to the correct class.
# Does this dynamic routing make perfect sense? If so, we are ready to move to Topic 3: The Liskov Substitution Principle (LSP)!