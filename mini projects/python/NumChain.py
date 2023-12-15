def number_chain():
    c = 1
    while True:
        s = ""
        for i in range(1, c + 1):
            s += f"{c}\t"
        yield s
        c += 1


nc = number_chain()
for i in range(10):
    print(next(nc))
