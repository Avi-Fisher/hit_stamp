import random
from random import  randint

def generate_secret(length):
    secret = ""


    while len(secret) < 4:
        number = randint(0, 9)

        if str(number) not in secret:
            secret += str(number)


    return secret

print(generate_secret(4))