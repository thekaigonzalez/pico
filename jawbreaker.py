# JawBreaker & GobStopper v1

# JawBreaker - industry password cracker
# GobStopper - quick character guessing algorithm

password_exist = "kaidan"

tries = 0

password = ""
password2 = ""
password3 = ""
password4 = ""
password5 = ""

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
    rand = string.ascii_lowercase  # + string.punctuation + string.digits + string.ascii_uppercase
    rage = [ch for ch in rand]
    gen = ""

    while (length < len):
        gen += random.choice(rage)
        length += 1

    return gen


print("guessing...")

attempts = 1
passwords = []
sets = 0

# JawBreaker
while (password_exist not in passwords):
    sets += 1;
    passwords = []
    while (len(passwords) < attempts):
        password_toadd = generate_password(len(password_exist))
        if (password_toadd in passwords):
            while (password_toadd in passwords):
                password_toadd = generate_password(len(password_exist))
        passwords.append(password_toadd)
    tries += attempts

print("password gessed! possibilities: " + " | ".join(passwords))
print("""
attempts: {}   
""".format(tries))
