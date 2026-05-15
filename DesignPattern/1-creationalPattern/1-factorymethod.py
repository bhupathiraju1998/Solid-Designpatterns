# Concept: A factory is a helper that makes the right kind of object for you so your main code doesn't have to decide which specific class to instantiate


from abc import ABC, abstractmethod

# -----------------------------
# Strategy Interface
# -----------------------------
class NotificationStrategy(ABC):
    @abstractmethod
    def send(self, message: str) -> str:
        pass


# -----------------------------
# Concrete Strategies
# -----------------------------
class EmailStrategy(NotificationStrategy):
    def send(self, message: str) -> str:
        return f"Email sent: {message}"


class SMSStrategy(NotificationStrategy):
    def send(self, message: str) -> str:
        return f"SMS sent: {message}"


# -----------------------------
# Optional Factory (clean registry approach)
# -----------------------------
class StrategyFactory:
    _registry = {
        "email": EmailStrategy,
        "sms": SMSStrategy
    }

    @staticmethod
    def get_strategy(strategy_type: str) -> NotificationStrategy:
        try:
            return StrategyFactory._registry[strategy_type]()
        except KeyError:
            raise ValueError(f"Unknown strategy type: {strategy_type}")


# -----------------------------
# Service (Dependency Injection target)
# -----------------------------
class NotificationService:
    def __init__(self, strategy: NotificationStrategy):
        self.strategy = strategy  # injected dependency

    def notify(self, message: str) -> str:
        return self.strategy.send(message)


# -----------------------------
# Usage
# -----------------------------

# Using direct DI
email_service = NotificationService(EmailStrategy())
print(email_service.notify("Welcome to the platform!"))

sms_service = NotificationService(SMSStrategy())
print(sms_service.notify("Your OTP is 1234"))

# Using Factory + DI
strategy = StrategyFactory.get_strategy("email")
service = NotificationService(strategy)
print(service.notify("Factory-created email message"))