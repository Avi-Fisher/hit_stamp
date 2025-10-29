from bulls_and_cows.game.io import pormpt_guess
from bulls_and_cows.game.logic import score_guess, init_state, apply_guess, is_won
from bulls_and_cows.game.secret import generate_secret


def play():

    secret = generate_secret(4)
    state = init_state(secret,4,10)


    while True:
        guess = pormpt_guess(state["length"])
        apply_guess(state,guess)

        print(state["history"])
        if is_won(state["history"][-1][1],state["length"]):
            print("you win!!!!!!")
            exit("goodbye")

        if state["max_tries"] == state["tries_used"]:
            print("you loserrrrrrr!!!!!!")
            exit("goodbye")






















if __name__ == "__main__":
    play()

















