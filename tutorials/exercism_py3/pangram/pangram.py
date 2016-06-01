
# -*- coding: UTF-8 -*-

import re 

def is_pangram(s):
    
    letters = re.sub('[^a-zA-Z]','',s)
   
    return len(list(set(letters.lower())))== 26 
     
