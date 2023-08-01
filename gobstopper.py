# JawBreaker & GobStopper v1

# JawBreaker - industry password cracker
# GobStopper - quick character guessing algorithm

password_exist = "hello12321312314412"

tries = 0

password = ""

import random
import string
import time
import threading

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
    rand = string.ascii_lowercase#  + string.punctuation + string.digits + string.ascii_uppercase 
    rage = [ch for ch in rand]
    gen = ""


    while (length < len):
        gen += random.choice(rage)
        length += 1

    return gen
    
print("guessing...")

pchar = ""
index = 0;

while (not password == password_exist):
    pchar = generate_password(1)
    if (pchar == password_exist[index]):
        index+=1;
        password+=pchar

print("password guessed! " + password)
