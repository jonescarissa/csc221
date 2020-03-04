''' Regex Version of strip
Author: Carissa Jones
'''

import re

def restrip(s, chars = None):
    '''Given a string, do the same thing as the strip() string 
    method. If no other agruments are passed other than the string, 
    then whitespace characters will be removed from the beginning and 
    end of the string. Otherwise, the characters specified in the
    second argument to the function will be removed from the
    string.'''
    if chars == None:
        strip_left = re.compile(r'^\s*')
        strip_right = re.compile(r'\s*$')

        s = re.sub(strip_left, "", s)
        s = re.sub(strip_right, "", s)

    else:
        print(re.escape(chars))
        strip_left = re.compile(r'^[' + re.escape(chars) + r']*')
        strip_right = re.compile(r'[' + re.escape(chars) + r']*$')
        s = re.sub(strip_left, "", s)
        s = re.sub(strip_right, "", s)
    return s

print(restrip)




