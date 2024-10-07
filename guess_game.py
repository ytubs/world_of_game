import random
import time

from app import get_user_input_validate_with_message
from app import selected_difficulty

selected_difficulty = 5
def generate_random_secret():
    print('Generating Ultra Secret random number...')
    time.sleep(2)
    print('Done!')
    time.sleep(1)
    return random.randint(0,selected_difficulty)

def get_guess_from_user():
    return get_user_input_validate_with_message(selected_difficulty,f"Submit your guess! Must be between 0 to {selected_difficulty}\n")




def compare_input_to_secret(secret,input):
    print('Comparing your guess with the super duper secret number...')
    time.sleep(2)
    return secret == input

def play():
    print('''Welcome to the Guess Game!
    We will now generating a secret number!
    ''')
    secret_number = generate_random_secret()
    print(secret_number)
    usr_input = get_guess_from_user()
    if compare_input_to_secret(secret_number,usr_input):
        print('you are correct!')
    else:
        print('You LOSE!!! HAHAHAH')

play()



