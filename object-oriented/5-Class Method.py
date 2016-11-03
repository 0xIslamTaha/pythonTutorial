# Goal: Define the class method.
# The class method is using for attribute constructor


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

    # Regular method
    # Take an object as the first argument.
    # Operate on the objects' attributes
    def return_full_description(self):
        return [self.name, self.mail, self.job]

    #Class Method
        # Start with @classmethod decoration.
        # Take a class as the first argument.
        # Do some process
        # return the class init method
    @classmethod
    def describe_class_method(cls, data):
        name, mail, job = data.split('-')
        print cls.General_Info
        return cls(name, mail, job)

# Regular way to create the object
object_1 = Human('Islam Taha', 'islamtaha2012@gmail.com', "Automation Software Test")
print object_1.return_full_description()

# Another method to create the object using the second constructor method
object_2 = Human.describe_class_method('Islam Taha-islamtaha2012@gmail.com-Automation Software Test')
print object_2.return_full_description()
