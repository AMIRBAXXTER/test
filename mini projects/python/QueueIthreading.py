from threading import Thread
from time import sleep
from queue import Queue

q = Queue()


def show_number(i):
    while True:
        number = q.get()
        sleep(0.1)
        print(f"\nthread number {i}, number:{number},remain:{q.qsize()}")
        q.task_done()
        if q.empty():
            break


num_list = [i for i in range(101)]
for i in num_list:
    q.put(i)

for th in range(1, 5):
    thread = Thread(target=show_number, args=(th,))
    thread.start()
