# Anton Ilic, completed Apr 1, 2023
# Updated code to be more concise and legible Sat. Feb 15th
# https://projecteuler.net/problem=19


def isLeapYear(year):
    '''
    Checks if the year is a leap year.
    A leap year is defined as being divisible by 4 but not 100 except when divisible by 400
    '''
    return ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)


def findTotalSundays(startDay, startYear):
    '''Finds total Sundays that fall on the 1st of a month in the 20th century '''
    endYear = 2000
    solution = 0
    day = startDay  # 1: Monday, 7: Sunday
    days = [31, 28, 31, 30, 31, 30, 31, 31,
            30, 31, 30, 31]  # days in each month

    for year in range(startYear, endYear + 1):
        for month in range(12):
            if day == 7:
                solution += 1

            if month == 1 and isLeapYear(year):
                daysinmonth = 29
            else:
                daysinmonth = days[month]

            currentday = (day + daysinmonth) % 7
            if currentday == 0:
                day = 7
            else:
                day = currentday

    return solution


print(findTotalSundays(2, 1901))  # starts on a tuesday
