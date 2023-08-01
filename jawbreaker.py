# JawBreaker & GobStopper v1

# JawBreaker - industry password cracker
# GobStopper - quick character guessing algorithm

# if your password has chracters make sure to change the rand variable and add your corresponding characters.
password_exist = "TYPE YOUR PASSWORD HERE"

tries = 0

import random
import string
import time
import threading


def generate_password(len):
    """
    Generates a password

    When this algorithm is run, it will use a range with 1-9, [a-Z], and extra symbols, and create
    an array based on that string, then it will check the length, and continue adding random characters from the
    character array.
    
    """
    import random

    length = 0

    # by default it will only guess lowercase passwords
    rand = string.ascii_lowercase  # + string.punctuation + string.digits + string.ascii_uppercase
    rage = [ch for ch in rand]
    gen = ""

    while (length < len):
        gen += random.choice(rage)
        length += 1

    return gen


print("guessing...")

attempts = 1000
passwords = []
sets = 0

# JawBreaker
# while the password isn't in the passwords array
while (password_exist not in passwords):
    sets += 1;
    passwords = [] # if you don't want the passwords array to reset to save memory
    # while the amount of generations less than the specified amount
    # NOTE: higher attempt amount, covers more passwords but is slower.
    while (len(passwords) < attempts):
        # generating the password
        password_toadd = generate_password(len(password_exist))
        if (password_toadd in passwords): # if the password is already in the array (no doubling)
            while (password_toadd in passwords):
                password_toadd = generate_password(len(password_exist))
        passwords.append(password_toadd)
    tries += attempts

print("password gessed! possibilities: " + " | ".join(passwords))
print("""
attempts: {}   
""".format(tries))
