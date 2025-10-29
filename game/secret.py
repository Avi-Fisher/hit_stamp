import random
from random import  randint

def generate_secret(length):
    secret = ""
    count = 0

    while count < 4:
        number = randint(0, 9)

        if str(number) not in secret:
            secret += str(number)
            secret += " "
            count += 1

    return secret

