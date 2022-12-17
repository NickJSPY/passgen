from base64 import urlsafe_b64decode
from http.client import REQUEST_ENTITY_TOO_LARGE
from optparse import check_builtin
import random
import string
from urllib import request
import os
os.system("color 3")
print("Welcome to the DevSnake Password maker.")

def gen():
    import random

    upper_letter = 'ABCDEFGHIJKLMMOPQRSTUVWXYZ'
    lower_letter = "abcdefghijklmnopqurtuvwxyz"
    digits = '1234567890'
    symbols = '!@#$%^&*()<>?:[]/.,'

    numbtogen = input('How many password would you like to generate? >  ')
    upper, lower, nums, symbs = True, True, True, True,
    all = ""

    if upper:
        all += upper_letter
    if lower:
        all += lower_letter
    if nums:
        all += digits
    if symbs:
        all += symbols

        length = 28
        ammount = numbtogen
        
        for x in range(int(numbtogen)):
            password = ''.join(random.sample(all, length))
            print('Password: '+password)
        


    

gen()
gen()
gen()