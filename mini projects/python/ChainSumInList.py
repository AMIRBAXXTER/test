li = [1, 2, 3, 4, 5, 6, 7, 8]


def sum_gen(list2):
    i = 0
    for t in range(len(list2)):
        i += list2[t]
        yield i
        t += 1


sum2 = sum_gen(li)
for i in range(len(li)):
    print(next(sum2))
