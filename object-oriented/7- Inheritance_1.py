# Goal: Define the inheritance concept
    # Concept_1 : You can re-use the parent class (super class) methods and variables inside another class (sub class).


class Human(object):
    General_Info = 'PythonTutorial-BY-IslamTaha'

    def __init__(self, name, mail, job):
        self.name = name
        self.mail = mail
        self.job = job

    def return_full_description(self):
        return [self.name, self.mail, self.job]

    @classmethod
    def describe_class_method(cls, data):
        name, mail, job = data.split('-')
        # call static method inside a class method
        print cls.get_copy_rights()
        return cls(name, mail, job)

        # Static method:
        # Doesn't take class or object.

    @staticmethod
    def get_copy_rights():
        print 'Copy rights : Islam Taha'


# Inheritance from a super class
class Developer(Human):
    pass


print '# Create a developer object class will automatically call the __init__ method from the Developer class, ' \
      'If there is no __init__ inside it, it will look for __init__ inside the super class. '
developer_object = Developer('Islam Taha', 'islamtaha2012@gmail.com', "Automation Software Test")
