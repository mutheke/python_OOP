# Base class
class Vehicle:
    def __init__(self, name):
        self.name = name  # Encapsulation: keeping vehicle name private

    def move(self):
        raise NotImplementedError("This method should be overridden by subclasses")

# Car class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, name, model):
        super().__init__(name)  # Initialize the base class constructor
        self.model = model  # Model specific to the car

    def move(self):
        # Overriding the move method to provide car-specific behavior
        return f"The {self.name} car is driving 🚗"

# Plane class inheriting from Vehicle
class Plane(Vehicle):
    def __init__(self, name, airline):
        super().__init__(name)  # Initialize the base class constructor
        self.airline = airline  # Airline specific to the plane

    def move(self):
        # Overriding the move method to provide plane-specific behavior
        return f"The {self.name} plane is flying ✈️"

# Creating objects and demonstrating polymorphism
def demo_polymorphism():
    vehicles = [
        Car("Toyota", "Corolla"),
        Plane("Boeing", "Airways")
    ]
    
    for vehicle in vehicles:
        print(vehicle.move())  # Each vehicle moves differently based on its class

# Running the polymorphism demo
demo_polymorphism()
