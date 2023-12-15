from threading import Thread
from time import sleep


def pow10(num):
    sleep(2)
    print(f"\n{num}")


th = [Thread(target=pow10, args=[i]) for i in range(50)]
lst = []
for t in th:
    lst.append(t)
    t.start()

for tr in lst:
    tr.join()


print("threading is finished")
