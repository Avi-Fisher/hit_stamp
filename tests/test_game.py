from bulls_and_cows.game.logic import score_guess, init_state, apply_guess
from bulls_and_cows.game.secret import generate_secret
from bulls_and_cows.game.validate import is_valid_game

secret = generate_secret(4)
print(secret)
state = init_state(secret,4,10)
print(state)
guess = "1234"
apply_guess(state,guess)
print(state)
