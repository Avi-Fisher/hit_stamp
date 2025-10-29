import random
from random import  randint

def generate_secret(length):
    secret = ""

    while len(secret) < length:
        number = randint(0, 9)

        if str(number) not in secret:
            secret += str(number)


    return secret

