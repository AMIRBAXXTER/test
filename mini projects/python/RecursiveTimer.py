from time import sleep
ti = int(input("enter your time:"))


def timer(number):
    if number <= 0:
        print("your timer is end")
        return 0
    print(number)
    sleep(1)
    return timer(number-1)


print(timer(ti))
