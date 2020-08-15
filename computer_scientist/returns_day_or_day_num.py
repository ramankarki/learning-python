
def week(day, count=0):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if check_if_int(day) and int(day) < 7:
        number = int(day) + count % 7
        if number > 6:
            return days[number - 7]
        return days[number]
        
    elif day in days:
        number = days.index(day)
        number = number + count % 7
        if number > 6:
            return number - 7
        return number


def check_if_int(day):
    try:
        day = int(day)
        return True
    except:
        return False


if __name__ == "__main__":
    day = week(input("Day: ")).title()
    print(day)