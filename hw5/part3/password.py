'''Strong Password Detection
Author: Carissa Jones
'''

import pyperclip
import re

passwordRegex = re.compile(r'''(
    ^(?=.*[A-Z])  # at least one captial letter
    (?=.*[!@#$&*])       # at least one of these special characters
    (?=.*[0-9].*[0-9])   # at least two numbers
    (?=.*[a-z].*[a-z])   # at least two lower case letters
    .{10,}               # at least 10 total
    $
)''', re.VERBOSE)

def strong_password():
    '''Given a string, return True if is strong, False otherwise
    A strong password is defined as one that is at least eight 
    characters long, contains both uppercase and lowercase 
    characters, and has at least one digit.'''
    pword = input('Enter a strong password: ')
    mo = passwordRegex.search(pword)
    if (not mo):
        print('Not strong enough')
        return False
    else:
        print('Strong enough')
        return True

strong_password()

