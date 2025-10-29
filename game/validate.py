def is_valid_game(guess,length):
    check_dubll = set()

    if type(guess) == str:

        for i in guess:
            check_dubll.add(i)

            if len(check_dubll) == length:
                return True

    return False

def is_new_guess(guess,history):
    if guess in history:
        return False

    return True




