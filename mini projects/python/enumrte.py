list_ = ["amir", "mmd", "reza", "hamid"]
list2 = [1, 3, 4, 5, 7, 8]


def enu(li, start=0):
    c = start
    for i in li:
        index = (c, li[c])
        yield index
        c += 1


print(list(enu(list_)))

