def is_valid_game(guess,length):
    if type(guess) == int:
        if len(guess) == 4:
            for i in range(10):
                if str(i) * 2 not in guess:
                    return True

    return False

def is_new_guess(guess,history):
    if guess in history:
        return False

    return True