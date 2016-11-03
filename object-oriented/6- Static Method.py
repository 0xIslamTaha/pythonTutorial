# Goal: Define the static method.
# The static method is using to do a local process without change any class or instance.


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


object_1 = Human('Islam Taha', 'islamtaha2012@gmail.com', "Automation Software Test")
print object_1.return_full_description()

