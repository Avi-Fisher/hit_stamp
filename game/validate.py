def is_valid_game(guess,length):
    check_dubll = set()

    try:
        int(guess)
        for i in guess:
            check_dubll.add(i)

            if len(check_dubll) == length:
                return True
    except:
        pass
    return False

def is_new_guess(guess,history):
    if guess in history:
        return False

    return True




