import random
import time

from app import get_user_input_validate_with_message


def generate_random_secret(difficulty):
    print('Generating Ultra Secret random number...')
    time.sleep(1)
    print('Done!')
    time.sleep(1)
    return random.randint(0, difficulty)


def get_guess_from_user(difficulty):
    return get_user_input_validate_with_message(difficulty, f"Submit your guess! Must be between 0 to {difficulty}\n", "input is invalid or out of bounds! Try again.")


def compare_input_to_secret(secret, user_input):
    print('Comparing your guess with the super duper secret number...')
    time.sleep(1)
    return secret == user_input


def play(difficulty):
    print('''Welcome to the Guess Game!
    We will now generating a secret number!
    ''')
    secret_number = generate_random_secret(difficulty)
    usr_input = get_guess_from_user(difficulty)
    if compare_input_to_secret(secret_number, usr_input):
        print('you are correct! You WIN!')
    else:
        print('You LOSE!!!')
