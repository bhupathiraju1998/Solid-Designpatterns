
# “Encapsulate interchangeable behaviors and switch them dynamically.”
from abc import ABC, abstractmethod


# -----------------------------
# Strategy Interface
# -----------------------------
class PaymentStrategy(ABC):

    # Why we wrote this line:
    # All payment strategies must implement pay().
    @abstractmethod
    def pay(self, amount):
        pass


# -----------------------------
# Concrete Strategies
# -----------------------------
class CreditCardPayment(PaymentStrategy):

    # Why we wrote this line:
    # Credit card-specific payment behavior.
    def pay(self, amount):

        return f"Paid ₹{amount} using Credit Card"


class PayPalPayment(PaymentStrategy):

    # Why we wrote this line:
    # PayPal-specific behavior.
    def pay(self, amount):

        return f"Paid ₹{amount} using PayPal"


class CryptoPayment(PaymentStrategy):

    # Why we wrote this line:
    # Crypto-specific behavior.
    def pay(self, amount):

        return f"Paid ₹{amount} using Cryptocurrency"


# -----------------------------
# Context
# -----------------------------
class ShoppingCart:

    # Why we wrote this line:
    # Context receives strategy dynamically.
    def __init__(self, payment_strategy):

        self.payment_strategy = payment_strategy

    # Why we wrote this line:
    # Context delegates behavior to strategy.
    def checkout(self, amount):

        return self.payment_strategy.pay(amount)


# -----------------------------
# Usage
# -----------------------------

# Credit card strategy
cart1 = ShoppingCart(CreditCardPayment())

print(cart1.checkout(500))

print("-----")

# PayPal strategy
cart2 = ShoppingCart(PayPalPayment())

print(cart2.checkout(1000))

print("-----")

# Crypto strategy
cart3 = ShoppingCart(CryptoPayment())

print(cart3.checkout(2500))