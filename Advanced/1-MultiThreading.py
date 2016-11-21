'''
Steps :
    1- Create a queue
    2- Put jobs inside the queue
    3- create work() method:
        - get the job
        - Process the job
        - raise task_done
    4- Create and start the threads
'''

import Queue
import threading
import requests

# Create queue
q = Queue.Queue()

# Insert Jobs
q.put('http://google.com')
q.put('http://yahoo.com')
q.put('http://msn.com')

# Create work method
def work():
    # make sure that there is jobs
    while not q.empty():
        # pop from the queue
        url = q.get()

        # start job processing
        responce = requests.get(url)
        print responce.status_code, threading.current_thread().name, responce.url

        # raise flag that this job is done
        q.task_done()

# Create workers loop and target work method
for _ in range(2):
    # NOTE : We set work not work() as a target
    thread = threading.Thread(target=work)
    # start the thread
    thread.start()

for _ in range(10):
    print "I'm working in parallel with threads too"

# If You need to block code until the queue is empty.
q.join()
for _ in range(10):
    print ('I have to wait until the queue be empty')
