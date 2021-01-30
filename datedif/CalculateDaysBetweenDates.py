def main():
    print("Welcome to the date difference calculator \n\n"
          "This application is designed to calculate the difference between two dates in terms of days\n"
          "Please enter the date as integers / numbers\n")
    startYear = int( input("Please enter the start year:") )
    startMonth = int( input("Please enter the start month:") )
    startDay = int( input("Please enter the start day:") )

    endYear = int (input("\nPlease enter the end year:") )
    endMonth = int (input("Please enter the end month:") )
    endDay = int ( input("Please enter the end day:") )

    dateDifference = daysBetweenDates(startYear, startMonth, startDay, endYear,endMonth, endDay)
    print("\nThe days between these two dates is: " + str(dateDifference) )

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between the two input dates Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    total_days = 0
    while not areDatesEqual(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        total_days += 1
    # YOUR CODE HERE!
    return total_days

def areDatesEqual(year1, month1, day1, year2, month2, day2):
    """Returns true if the input dates are equal and false if they are not"""
    if year1 == year2 and month1 == month2 and day1 == day2:
        return True
    else:
         return False

def nextDay(year, month, day):
    """Increments the date input to the next day, modulus of the month and year """
    if month < 12 and day == daysInMonth(year, month):
        return year, month + 1, 1
    elif month == 12 and day == daysInMonth(year, month):
        return year + 1, 1, 1
    else:
        return year, month, day + 1

def daysInMonth(year, month):
    """Returns the days in a month, adjusting the days in February if the year is a leap year"""
    daysInEachMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(year):
        daysInEachMonth[1] = 29
    return daysInEachMonth[month - 1]

def isLeapYear(year):
    """Returns a true value if the year is a leap year and false if it is not"""
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

if __name__ == "__main__":
    main()
