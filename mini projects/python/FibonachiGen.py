def fibonachi():
    i = 0
    yield i
    j = 1
    yield j
    while True:
        k = i + j
        i = j
        j = k
        yield k


f = fibonachi()
for i in range(15):
    print(next(f))
