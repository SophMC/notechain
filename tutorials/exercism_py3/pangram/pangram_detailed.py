
# -*- coding: UTF-8 -*-

import re

def is_pangram(s):
    
      
    # create a regular expression object(regex) to pull out only letters 
    # from chars. ^ matches start of the string.
    regex = re.compile('[^a-zA-Z]')
    
    # Use regex object to substitute anything that doesn't match the pattern.
    # is the same as  letters = re.sub('[^a-zA-Z]','',s)
    letters = regex.sub('', s)
    
          
    #break up the sentence into characters and extract the unique values
    if len(list(set(letters.lower())))== 26: 
        
        print(list(set(letters)))
        print('This is a pangram')
        return True
    else: 
        print(list(set(letters)))
        print('This is not a pangram')
        return False  


if __name__ == '__main__':
    
    #is_pangram('the quick brown fox jumps over the lazy dog')
    is_pangram('Victor jagt zwölf Boxkämpfer quer über den großen Sylter' 
               'Deich.')
    
#set(list(s.lower())) >= set(ALPHABET)