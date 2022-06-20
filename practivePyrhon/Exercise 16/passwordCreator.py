import string
import random

def password():
    i = 0
    passwordRandom = []
    while i < 6:
        lower = string.ascii_lowercase
        passwordRandom += random.choice(lower)
        i += 1
    while i < 8:
        upper = string.ascii_uppercase
        passwordRandom += random.choice(upper)
        i += 1
    while i < 10:
        passwordRandom.append(str(random.randint(1,9)))
        i += 1
    return ("".join(passwordRandom))

print(password())