# Goal: Define the inheritance concept
# You can re-use the a class (super class) inside another class (sub class).
# sub-class have all things inside the super-class
# sub-class can over write any method inside the super class
# sub-class object's attributes are the attributes of super-class objects and the new attributes which are defined
# inside the sub-class


class Human(object):
    General_Info = 'PythonTutorial-BY-IslamTaha'

    def __init__(self, name, mail, job):
        self.name = name
        self.mail = mail
        self.job = job

    def return_full_description(self):
        # call static method inside the regular method
        self.get_copy_rights()
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


##############################################################################################################
# Inheritance from a super class
class Developer_1(Human):
    pass


print '# Create a developer object class will automatically call the __init__ method from the Developer_1 class, ' \
      'If there is no __init__ indie it, Will look for __init__ inside the super class. '

developer_object_1 = Developer_1('Islam Taha', 'islamtaha2012@gmail.com', "Automation Software Test")
print developer_object_1.return_full_description()
print '\n'

##############################################################################################################

##############################################################################################################
# Inheritance from a super class
# Over write the __init__method
class Developer_2(Human):
    # over write the __init__ method
    def __init__(self):
        print 'overwrite the super class init method'

developer_object_2 = Developer_2()


##############################################################################################################

##############################################################################################################
# Inheritance from a super class
# update the __init__ method
class Developer_3(Human):
    # over write the __init__ method
    def __init__(self, name, mail, job):
        super(Developer_3, self).__init__(name, mail, job)
        print 'overwrite the super calss init method'

print 'Over write the __init__ method'
developer_object_3 = Developer_3('Islam Taha', 'islamtaha2012@gmail.com', "Automation Software Test")
print '# use a method from the super class'
print developer_object_3.return_full_description()
##############################################################################################################
