# An object changes its behavior when its internal state changes.”
# Idle state → waiting for money
# HasMoney state → waiting for selection
# Dispensing state → giving product
from abc import ABC, abstractmethod


# -----------------------------
# State Interface
# -----------------------------
class State(ABC):

    @abstractmethod
    def publish(self, document):
        pass


# -----------------------------
# Concrete States
# -----------------------------
class DraftState(State):

    def publish(self, document):
        print("Moving from DRAFT → MODERATION")
        document.state = ModerationState()


class ModerationState(State):

    def publish(self, document):
        print("Moving from MODERATION → PUBLISHED")
        document.state = PublishedState()


class PublishedState(State):

    def publish(self, document):
        print("Already PUBLISHED. No further changes allowed.")


# -----------------------------
# Context
# -----------------------------
class Document:

    def __init__(self):
        self.state = DraftState()  # initial state

    def publish(self):
        self.state.publish(self)


# -----------------------------
# Usage
# -----------------------------
doc = Document()

doc.publish()  # Draft → Moderation
doc.publish()  # Moderation → Published
doc.publish()  # Already Published