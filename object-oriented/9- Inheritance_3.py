# Goal: Define the inheritance concept
# Concept_3 : sub-class object's attributes are the attributes of super-class objects and the new attributes which are defined
# inside the sub-class


class Human(object):
    General_Info = 'PythonTutorial-BY-IslamTaha'

    def __init__(self, name, mail, job):
        self.name = name
        self.mail = mail
        self.job = job

    def return_full_description(self):
        # call static method inside the regular method
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
# Over write the __init__method
class Developer(Human):
    # over write the __init__ method
    def __init__(self, name, mail, job):
        # call the super calss init method
        super(Developer, self).__init__(name, mail, job)

    def Developer_new_method(self):
        print 'This is a Developer class method and can only be called usign the Developer object'

human_objectg = Human('Islam Taha', 'islamtaha2012@gmail.com', "Automation Software Test")
print '# call Human object return_full_description method'
print human_objectg.return_full_description()

print '\n'
developer_object = Developer('Islam Taha', 'islamtaha2012@gmail.com', "Automation Software Test")
print '# call Developer object return_full_description method, which is not defined inside the Developer class,' \
      ' so python will look for it in the super class'
print developer_object.return_full_description()

print '\n'
print '# Call sub-class method'
developer_object.Developer_new_method()
