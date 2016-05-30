
def is_leap_year(year):
    if (year%400 !=0) & (year%4 != 0) & (year%100 != 0):
        print ("%d is not a leap year" % year)
        return False
    else:
        print ("%d is a leap year!" % year)
        return True

year = int(input('Type in a year to test if it is a leap year\n> '))  
is_leap_year(year)