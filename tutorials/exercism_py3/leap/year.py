
def is_leap_year(year):
    
    b = (year%4 ==0)
    c = (year%100 != 0)
    d = (year%400 == 0)
    
    if b == True and c == True or d == True:
        print ("%d is a leap year! "% year)
        return True
      
    else: 
        print ("%d is not a leap year" % year)
        return False

if __name__ == '__main__':
  
    year = int(input('Type in a year to test if it is a leap year\n> '))  
    is_leap_year(year)
    
 