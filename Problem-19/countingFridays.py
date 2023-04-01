# Anton Ilic, completed Apr 1, 2023
# https://projecteuler.net/problem=19


def isLeapYear(year):
    '''Check if the year is a leap year'''
    if (((str(year))[len(str(year))-3:len(str(year))-1]) == '00'):
        if (year % 400 == 0):
            return True
    elif (year % 4 == 0):
        return True
    else:
        return False


def addToDayOfTheWeek(dayOfTheWeekChosen):
    '''Returns day of the week, as a number'''
    return (dayOfTheWeekChosen + 1 if dayOfTheWeekChosen + 1 <= 7 else 1)


def findTotalSundays(dayOfTheWeekStart, startYear):
    '''Finds total Sundays that fall on the 1st of a month in the 20th century '''
    totalSundaysOnFirst = 0
    dayOfTheWeek = dayOfTheWeekStart
    year = startYear
    while (year <= 2000):
        for month in range(1, 13):
            if month == 9 or month == 4 or month == 6 or month == 11:
                for day in range(1, 31):
                    if (day == 1 and dayOfTheWeek == 7):
                        totalSundaysOnFirst += 1
                    dayOfTheWeek = addToDayOfTheWeek(dayOfTheWeek)
            elif month == 2:
                if isLeapYear(year):  # in case of a leap year, 31 days of feb2
                    for day in range(1, 30):
                        if (day == 1 and dayOfTheWeek == 7):
                            totalSundaysOnFirst += 1
                        dayOfTheWeek = addToDayOfTheWeek(dayOfTheWeek)
                else:
                    for day in range(1, 29):
                        if (day == 1 and dayOfTheWeek == 7):
                            totalSundaysOnFirst += 1
                        dayOfTheWeek = addToDayOfTheWeek(dayOfTheWeek)
            else:
                for day in range(1, 32):
                    if (day == 1 and dayOfTheWeek == 7):
                        totalSundaysOnFirst += 1
                    dayOfTheWeek = addToDayOfTheWeek(dayOfTheWeek)

        year += 1
    return totalSundaysOnFirst


print(findTotalSundays(2, 1901))
