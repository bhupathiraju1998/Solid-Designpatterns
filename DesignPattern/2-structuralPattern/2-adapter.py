# “Convert one interface into another interface that the client expects.”
# “Wrap incompatible objects so they can work with your existing system.”
from abc import ABC, abstractmethod


# -----------------------------
# Target Interface
# -----------------------------
class Notification(ABC):

    # Why we wrote this line:
    # Our application expects ALL notifications to use send().
    @abstractmethod
    def send(self, message):
        pass


# -----------------------------
# Existing Third-Party Class
# -----------------------------
class OldEmailService:

    # Why we wrote this line:
    # Third-party library uses incompatible method name.
    def send_email(self, content):
        return f"Old Email Service sending: {content}"


# -----------------------------
# Adapter
# -----------------------------
class EmailAdapter(Notification):

    # Why we wrote this line:
    # Adapter wraps the incompatible object.
    def __init__(self, old_email_service):

        self.old_email_service = old_email_service

    # Why we wrote this line:
    # Adapter translates expected send()
    # into send_email().
    def send(self, message):

        return self.old_email_service.send_email(message)


# -----------------------------
# Usage
# -----------------------------

# Existing incompatible object
old_service = OldEmailService()

# Wrap it inside adapter
adapter = EmailAdapter(old_service)

# Application uses standard interface
print(adapter.send("Welcome to the platform!"))