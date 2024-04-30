from termcolor import colored
from time import sleep
import os
hour = int(input("enter Hour : "))
minute = int(input("enter Minute : "))
second = int(input("enter Second : "))
while hour != 0 or minute != 0 or second != 0:
    if second == -1:
        minute -= 1
        second = 59
    if minute == -1:
        hour -= 1
        minute = 59
    print(colored(f"{hour} : {minute} : {second}", "red"))
    sleep(1)
    os.system("clear")
    second -= 1
