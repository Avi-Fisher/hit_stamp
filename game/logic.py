def score_guess(secret,guess):
    bulls = 0
    cows = 0

    for i in range(4):
        if secret[i] == guess[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1

    return (bulls,cows)



    return "tuple"

def is_won(bulls,length):
    if bulls == length:
        return True
    return False



    return "bool"

def init_state(secret,length,max_tries):

    gamestate = {"secret":secret,
                 "length":length,
                 "max_tries":max_tries,
                 "tries_used":0,
                 "allow_leading_zero":bool,
                 "history":list,
                 "seen":set()}

    return





    return "state"

def apply_guess():
    return "tuple"



























