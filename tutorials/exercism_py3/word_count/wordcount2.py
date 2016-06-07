# -*- coding: utf-8 -*-

import re

def word_count(sentence):
    
    sentence = re.sub('[,_]',' ',sentence)
    
    # ^ to substitute things that are NOT \s(spaces) and \w(alphanumeric 
    #   characters-letters). r, means raw string notation.
    sentence = re.sub(r'[^\s\w_]+', '', sentence.lower())
    f = sentence.split()
      
    # Make a dictionary to store the pairs
    p = {}
    
    for x in f:
        
        # \b before and after helps to preserve whole words.
        matches = re.findall((r'\b%s\b'%x),' '.join(x for x in f))
        
        #match the key to the value in the dictionary
        p[x] = len(matches)

        return p    
  
                       
                       
                       