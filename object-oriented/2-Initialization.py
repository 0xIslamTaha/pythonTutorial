# Goals
# Create the constructor method for the class.
# Create an object variables


# Create a class
class Human(object):
    # Initialization method.
    # This is a constructor method which is called by default once you create an object from this class
    def __init__(self, name, mail, job):
        # Object variables
        # Create attributes for the object
        self.name = name
        self.mail = mail
        self.job = job

# Create objects from this class
# You have to bypass all values for the __init__ method.
object_1 = Human('Islam Taha', 'islamtaha2012@gmail.com', "Automation Software Test")
object_2 = Human('0', '0', '0')

print object_1  # This is an instance from the class
print object_2  # This is another instance from the class

print object_1.name  # This is the value of object parameter
print object_2.name  # AttributeError : cos the second object doen't have <name> attribute yet
