from bulls_and_cows.game.validate import is_valid_game


def pormpt_guess(length):
    while True:
        guess = input("enter your guess")

        if is_valid_game(guess,length):
            return guess
        print(f"please enter guess in length {length}")

def print_feesbace(guess,bulls,cows):

    print(guess)
    print(f"you have a {bulls} bulls")
    print(f"you have a {cows} cows")

def print_status(state):

    print(state["history"])
    print(f"your number guess is {state["tries_used"]}")



def print_result(state,win):
    print(state["history"])
    print(state["secret"])




















