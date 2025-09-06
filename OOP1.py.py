class Device:
    # The constructor for the base class.
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model

    # A generic method to turn on the device.
    def turn_on(self):
        print(f"The device {self.manufacturer} {self.model} is starting up....")


# The subclass 'Smartphone' inherits attributes from the parent class, it include additional attributes.
class Smartphone(Device):
    def __init__(self, manufacturer, model, operating_system):

        # super() is to call the parent class's constructor and initialize
        super().__init__(manufacturer, model)
        
        # add a new attribute specific to the Smartphone class.
        self.operating_system = operating_system

    # A method specific to the Smartphone class.
    def make_call(self):
        print(f"The {self.model} is making a call.")

    # Polymorphism: overriding the 'turn_on' method from the parent class.
    def turn_on(self):
        print(f"The smartphone {self.model} with {self.operating_system} is turning on...")
        print("You are connected.")

# instance of the base class Device
xiaomi = Device("redmi", "Galaxy")
xiaomi.turn_on()
print("-" * 20)

# instance of the subclass 'Smartphone'
# now with 3 arguments (manufacturer, model, operating_system)
smartphone = Smartphone("Nokia", "Military Version", "Bms")

# The 'smartphone' object can use methods from its own class...
smartphone.make_call()

# demonstrating polymorphism.
smartphone.turn_on()

# Accessing inherited attributes
print(f"Welcome to the {smartphone.model} from {smartphone.manufacturer}.")
