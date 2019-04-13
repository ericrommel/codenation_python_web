# You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises) leaving on day number 3 (a
# Wednesday). You return home after 137 sleeps. Write a general version of the program which asks for the starting
# day number, and the length of your stay, and it will tell you the name of day of the week you will return on.

def day_of_week(day):
    if day == 0:
        return "Sunday"
    elif day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    else:
        return "This number doesn't correspond to a valid day of week"

def will_return_on(start, length):
    return day_of_week((start + length) % 6)


start_day = int(input("Start day number[0-6]: "))
length_stay = int(input("Length of your stay: "))

print(will_return_on(start_day, length_stay))
