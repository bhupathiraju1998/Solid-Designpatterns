# “When one object changes state, automatically notify other dependent objects.”

from abc import ABC, abstractmethod


# -----------------------------
# Observer Interface
# -----------------------------
class Subscriber(ABC):

    # Why we wrote this line:
    # Every subscriber must implement update().
    @abstractmethod
    def update(self, video_title):
        pass


# -----------------------------
# Concrete Observers
# -----------------------------
class EmailSubscriber(Subscriber):

    # Why we wrote this line:
    # Each subscriber has its own identity.
    def __init__(self, email):

        self.email = email

    # Why we wrote this line:
    # Called automatically when subject sends notification.
    def update(self, video_title):

        print(f"Email sent to {self.email}: New video uploaded -> {video_title}")


class MobileSubscriber(Subscriber):

    def __init__(self, username):

        self.username = username

    def update(self, video_title):

        print(f"Mobile notification for {self.username}: {video_title}")


# -----------------------------
# Subject
# -----------------------------
class YouTubeChannel:

    # Why we wrote this line:
    # Store all registered observers.
    def __init__(self):

        self.subscribers = []

    # Why we wrote this line:
    # Allow observers to subscribe.
    def subscribe(self, subscriber):

        self.subscribers.append(subscriber)

    # Why we wrote this line:
    # Allow observers to unsubscribe.
    def unsubscribe(self, subscriber):

        self.subscribers.remove(subscriber)

    # Why we wrote this line:
    # Notify ALL observers automatically.
    def notify_subscribers(self, video_title):

        for subscriber in self.subscribers:

            subscriber.update(video_title)

    # Why we wrote this line:
    # Simulate new video upload event.
    def upload_video(self, video_title):

        print(f"\nNew Video Uploaded: {video_title}\n")

        self.notify_subscribers(video_title)


# -----------------------------
# Usage
# -----------------------------

# Create subject
channel = YouTubeChannel()

# Create observers
sub1 = EmailSubscriber("alice@example.com")
sub2 = MobileSubscriber("BobGaming")

# Register observers
channel.subscribe(sub1)
channel.subscribe(sub2)

# Trigger event
channel.upload_video("Observer Pattern Explained")
