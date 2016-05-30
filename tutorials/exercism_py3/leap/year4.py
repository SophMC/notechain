
def is_leap_year(year):
         
    if year % 4 ==0 and year % 100 != 0 or year % 400 == 0:
        print ("%d is a leap year! "% year)
        return True
      
    else: 
        print ("%d is not a leap year" % year)
        return False

if __name__ == '__main__':
  
    year = int(input('Type in a year to test if it is a leap year\n> '))  
    is_leap_year(year)
    
 