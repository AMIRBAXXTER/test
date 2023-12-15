def eo_gen(even_or_odd="even"):
    c = 0
    if even_or_odd == "odd":
        c = 1
    while True:
        yield c
        c += 2


evenodd = eo_gen("odd")
for i in range(10):
    print(next(evenodd))
