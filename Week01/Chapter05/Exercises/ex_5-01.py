# Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday.
# Write a function which is given the day number, and it returns the day name (a string).

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

for i in range(8):
    print(day_of_week(i))
