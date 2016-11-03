# Goal : Create the constructor method for the class


# Create a class
class Human(object):
    # Initialization method.
    # This is a constructor method which is called by default once you create an object from this calss
    def __init__(self, name, mail, job):
        # Object variables
        # Create attributes for the object
        self.name = name
        self.mail = mail
        self.job = job

    # Regular method
    # Take an object as the first argument.
    # Operate on the objects' attributes
    def return_full_description(self):
        return [self.name, self.mail, self.job]


# You have to bypass all values for the __init__ method.
object_1 = Human('Islam Taha', 'islamtaha2012@gmail.com', "Automation Software Test")
object_2 = Human('0', '0', '0')

# Correct Calling :
# The regular method is calling as an object attribute
print object_1.return_full_description()
# The regular method is calling using the class, but you have to pass object
print Human.return_full_description(object_1)

# Error : Regular method must be called with class objects as the first argument get self
try:
    print Human.return_full_description()
except TypeError:
    print NameError
