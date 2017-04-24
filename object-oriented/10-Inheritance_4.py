# Goal: Define the inheritance concept
# Concept_4 : Class variable is shared between childs.


class Human(object):
    General_Info = 'PythonTutorial-BY-IslamTaha'


class Child(Human):
    def understand_class_variable(self):

        print self.General_Info
        self.General_Info = 'child value.'
        print self.General_Info
        print Human.General_Info


class Child_2(Human):
    def __init__(self):
        Human.General_Info = 'CHILD 2'

o = Child()
o.understand_class_variable()

print '\n'
Human.General_Info = '@!#!@#!@#!@#!@#!@'
o.understand_class_variable()

print '\n'
o2 = Child_2()
print Human.General_Info
o.understand_class_variable()