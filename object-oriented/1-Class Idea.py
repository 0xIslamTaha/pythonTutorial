# This Example describe the defrance between class and object

# Create a class
class Human(object):
    pass

# Create objects from this class
object_1 = Human()
object_2 = Human()

# Object variables
# Create attributes for this object
object_1.name = 'Islam Taha'
object_1.mail = 'islamtaha2012@gmail.com'
object_1.job = "Automation Software Test"

print object_1 # This is an instance from the class
print object_2 # This is another instance from the class
print object_1.name # This is the value of object parameter

# Error
# AttributeError : cos the second object doesn't have <name> attribute yet
try:
    print object_2.name
except AttributeError:
    print NameError

