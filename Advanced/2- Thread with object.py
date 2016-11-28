import Queue
import threading
import requests
import random

class check(object):
    def __init__(self):
        print "I'm a unique object \n"
        self.list = [2]

    def appen_list(self):
        self.list.append(random.randint(1, 1000))
        print self.list
        print '\n'

def work():
    obj = check()
    obj.appen_list()

for _ in range(10):
    threading.Thread(target=work).start()
