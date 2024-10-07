import random
from app import get_user_input_validate_with_message

difficulty = 4

def generate_random_secret():
    return random.randint(0,difficulty)

def get_guess_from_user():
    return get_user_input_validate_with_message(difficulty,f"Submit your guess! Must be between 0 to {difficulty}")




def compare_input_to_secret():
    return generate_random_secret() == get_guess_from_user()


def play():
    compare_input_to_secret()




