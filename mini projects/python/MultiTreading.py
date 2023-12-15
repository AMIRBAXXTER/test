from threading import Thread
import time


def task(n):
    print(f"{n} : start\n")
    time.sleep(3)
    print(f"{n} : {n ** 50 * 54 / 98 ** 100}\n")


th = [Thread(target=task, args=[i]) for i in range(50)]
for i in th:
    i.start()
# for i in range(50):
#     task(i)
