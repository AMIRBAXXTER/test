from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        """THIS METHOD MUST SET"""

    @abstractmethod
    def repair(self):
        """THIS METHOD MUST SET"""


class LandVehicle(Vehicle):
    def move(self):
        print("driving...")

    def repair(self):
        print("repairing land vehicle...")

    @abstractmethod
    def brake(self):
        """THIS METHOD MUST SET"""


class AirVehicle(Vehicle):
    def move(self):
        print("flying...")

    def repair(self):
        print("repairing air vehicle...")

    @abstractmethod
    def eject(self):
        """THIS METHOD MUST SET"""


class Car(LandVehicle):
    def brake(self):
        print("braking...")


class AirPlane(AirVehicle):
    def eject(self):
        print("ejecting...")


lambo = Car()
lambo.repair()
lambo.brake()
lambo.move()
print("-" * 10, "=" * 10, "-" * 10, sep="")
f16 = AirPlane()
f16.repair()
f16.eject()
f16.move()
