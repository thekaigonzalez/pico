password_exist = "admin"

tries = 0

password = ""

import random
import string
import time

def generate_password(
    len): 
    """
    Generates a password

    When this algorithm is run, it will use a range with 1-9, [a-Z], and extra symbols, and create
    an array based on that string, then it will check the length, and continue adding random characters from the
    character array.
    
    """
    import random

    length = 0
    rand = string.ascii_lowercase
    rage = [ch for ch in rand]
    gen = ""


    while (length < len):
        gen += random.choice(rage)
        length += 1

    return gen
    
print("guessing...")
while (not password == password_exist):
    password = generate_password(len(password_exist));
    import os
    tries += 1
    if ((tries % 1000) == 0):
        time.sleep(2)
print("password gessed! " + password)
