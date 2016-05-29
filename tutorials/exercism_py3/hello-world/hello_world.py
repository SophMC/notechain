#
# Skeleton file for the Python "Hello World" exercise.
#
def hello(name=''):
   
    if name == '':
        greeting = "Hello, World!"
        print (greeting)
        return greeting
    
    else:
        greeting = 'Hello, %s!' % name
        print (greeting)
        return greeting

if __name__ == '__main__':
    
    name = input('What is your name?\n> ')
    hello(name)