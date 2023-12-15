def mazrab_3(number):
    if number < 3:
        return
    elif number % 3 == 0:
        print(number)
    mazrab_3(number - 1)


mazrab_3(100)
