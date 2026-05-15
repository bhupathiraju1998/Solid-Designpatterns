# “Store and manage objects/classes in a centralized lookup table.”
# avoaid if /else is main motto

from abc import ABC, abstractmethod


# -----------------------------
# Base Interface
# -----------------------------
class NotificationService(ABC):

    @abstractmethod
    def send(self, message):
        pass


# -----------------------------
# Concrete Services
# -----------------------------
class EmailService(NotificationService):

    def send(self, message):
        return f"Email sent: {message}"


class SMSService(NotificationService):

    def send(self, message):
        return f"SMS sent: {message}"


# -----------------------------
# Registry
# -----------------------------
class ServiceRegistry:

    # Why we wrote this line:
    # Central dictionary storing service mappings.
    _services = {}

    @classmethod
    def register(cls, key, service):

        # Why we wrote this line:
        # Add service into registry dynamically.
        cls._services[key] = service

    @classmethod
    def get_service(cls, key):

        # Why we wrote this line:
        # Validate requested key exists.
        if key not in cls._services:
            raise ValueError(f"Service '{key}' not found")

        # Why we wrote this line:
        # Return registered service object/class.
        return cls._services[key]


# -----------------------------
# Register Services
# -----------------------------

ServiceRegistry.register("email", EmailService())
ServiceRegistry.register("sms", SMSService())


# -----------------------------
# Usage
# -----------------------------

service = ServiceRegistry.get_service("email")

print(service.send("Welcome!"))