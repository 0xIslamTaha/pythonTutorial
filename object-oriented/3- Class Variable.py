# Goals
    # Define the class variable
    # Note that: The value of the class variable will be shared between all objects.
    # If you overwrite this value for any object (Polymorphism), This object only have this new value.

# Create a class
class Human(object):
    # Class Variable
    # Shared between all objects
    General_Info = 'PythonTutorial-BY-IslamTaha'

    # Initialization method.
    # This is a constructor method which is called by default once you create an object from this class
    def __init__(self, name, mail, job):
        # Object variables
        # Create attributes for the object
        self.name = name
        self.mail = mail
        self.job = job

        # Call The Class Variable inside methods
        Human.General_Info = Human.General_Info

        # Notes : Calling the class Variable using <self> will create an object variable with the same name
        self.General_Info = Human.General_Info

# Create objects from this class
# You have to bypass all values for the __init__ method.
object_1 = Human('Islam Taha', 'islamtaha2012@gmail.com', "Automation Software Test")
object_2 = Human(0, 0, 0)

# Call Calls Variable
print object_1.General_Info
print object_2.General_Info
print Human.General_Info
print '\n'

# Edit class variable for each object is equal to overwrite this object attribute
object_1.General_Info = 'object_1 Edit version'
# Call Calls Variable
print object_1.General_Info # This will call the modified one of object_1
print object_2.General_Info # This will call the original one
print Human.General_Info    # This will call the original one
print '\n'

# Edit class variable for each object is equal to overwrite this object attribute
Human.General_Info = 'object_1 Edit version'
# Call Calls Variable
print object_1.General_Info # This will call the modified one of object_1
print object_2.General_Info # This will call the original one
print Human.General_Info    # This will call the original one