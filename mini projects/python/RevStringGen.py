string = "mohadeseh pormahdi sigarodi"


def reversed_str(str):
    for i in range(len(str)-1, -1, -1):
        yield str[i]


rev = reversed_str(string)
for i in range(len(string)):
    print(next(rev))
