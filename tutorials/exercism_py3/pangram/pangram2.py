# -*- coding: UTF-8 -*-

ALPHABET = 'abcdefghijklmnopqrstuvwxyz '


def is_pangram(s):
    
     
    return set(list(s.lower())) >= set(ALPHABET)
  
if __name__ == '__main__':
    
    #is_pangram('the quick brown fox jumps over the lazy dog')
    # When I declare the encoding at the beginning, it doesnt throw up an error 
    # with string here.
    string = 'Victor jagt zwölf Boxkämpfer quer über den großen Sylter Deich.'
    #new = string.encode('utf-8')
    is_pangram(string)