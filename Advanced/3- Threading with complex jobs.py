import Queue
import threading
import requests

def complex_job(start_number):
    pass

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
