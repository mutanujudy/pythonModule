# Base Class
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        """Default move method (can be overridden in subclasses)."""
        print(f"{self.name} is moving.")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving on the road 🚗.")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying in the sky ✈️.")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing on the water 🚤.")

# Subclass: Bicycle
class Bicycle(Vehicle):
    def move(self):
        print(f"{self.name} is pedaling on the track 🚴.")

# Demonstrate Polymorphism
def demonstrate_movement(vehicle):
    vehicle.move()

# Create instances
car = Car("Tesla Model 3")
plane = Plane("Boeing 747")
boat = Boat("Speedboat")
bicycle = Bicycle("Mountain Bike")

# Demonstrating different move() methods
vehicles = [car, plane, boat, bicycle]
for v in vehicles:
    demonstrate_movement(v)
