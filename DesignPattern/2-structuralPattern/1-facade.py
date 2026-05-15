# -----------------------------
# Subsystem Classes
# -----------------------------
# “Hide a complicated subsystem behind one clean interface.”
class DVDPlayer:

    def on(self):
        print("DVD Player ON")

    def play(self, movie):
        print(f"Playing movie: {movie}")


class Projector:

    def on(self):
        print("Projector ON")

    def set_input(self):
        print("Projector input set to DVD")


class SoundSystem:

    def on(self):
        print("Sound System ON")

    def set_volume(self, level):
        print(f"Volume set to {level}")


class Lights:

    def dim(self):
        print("Lights dimmed")


# -----------------------------
# Facade
# -----------------------------

class HomeTheaterFacade:

    # Why we wrote this line:
    # Facade stores references to all subsystem objects.
    def __init__(self):

        self.dvd = DVDPlayer()
        self.projector = Projector()
        self.sound = SoundSystem()
        self.lights = Lights()

    # Why we wrote this line:
    # We provide ONE simple method hiding complex workflow.
    def watch_movie(self, movie):

        print("\nStarting movie night...\n")

        self.lights.dim()

        self.projector.on()
        self.projector.set_input()

        self.sound.on()
        self.sound.set_volume(10)

        self.dvd.on()
        self.dvd.play(movie)

        print("\nMovie setup complete!\n")


# -----------------------------
# Usage
# -----------------------------

home_theater = HomeTheaterFacade()

home_theater.watch_movie("Interstellar")