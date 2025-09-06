# --- Polymorphism with Vehicles ---

# The base class 'Vehicle' defines the common structure.
class Vehicle:
    # The 'move' method here does nothing. It serves as a guide for subclasses.
    def move(self):
        pass

# The 'Car' class inherits from 'Vehicle'.
class Car(Vehicle):
    # The 'move' method is implemented specifically for a car.
    def move(self):
        print("Car in motion ")

# The 'Boat' class inherits from 'Vehicle'.
class Boat(Vehicle):
    # The 'move' method is implemented specifically for a boat.
    def move(self):
        print("Boat in motion ")

# --- Polymorphism with Animals ---

# The base class 'Animal' defines the common structure.
class Animal:
    def move(self):
        pass

# The 'Snail' class inherits from 'Animal'.
class Snail(Animal):
    def move(self):
        print("The snail is crawling ")

# The 'Bird' class inherits from 'Animal'.
class Bird(Animal):
    def move(self):
        print("The bird is flying ")

# --- Polymorphism Demonstration ---

# Creating instances of each class.
my_car = Car()
my_boat = Boat()
my_snail = Snail()
my_bird = Bird()

# Placing the objects in a list to demonstrate polymorphism.
elements = [my_car, my_boat, my_snail, my_bird]

print("It's amazing! Different movements with the same method.")

# The loop calls the same 'move()' method on each object, but the behavior
# is different for each one.
for element in elements:
    element.move()
