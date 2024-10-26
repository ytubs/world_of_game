import random
import time
import sys
import os
from utils import get_user_input_validate_with_message, screen_cleaner


def generate_sequence(difficulty):
    sequence = [random.randint(1, 100) for _ in range(difficulty)]
    return sequence


def get_list_from_user(difficulty):
    print('Try to enter the numbers that were shown!')
    user_list = []
    for i in range(difficulty):
        user_list.append(get_user_input_validate_with_message(101, f'Enter number {i + 1}:\n'))
    return user_list


def is_list_equal(sequence, user_list):
    return sequence == user_list


def play(difficulty):
    print('''Welcome to Memory Game!
        We will now show you a sequence of numbers, you will then need to submit the numbers you remember''')
    sequence = generate_sequence(difficulty)
    print('---THE GENERATED SEQUENCE IS:---')
    time.sleep(2)
    for number in sequence:
        print(f'  {number}  ', end='')
    print('\n---END OF SEQUENCE---')

    time.sleep(0.7)
    screen_cleaner()

    user_list = get_list_from_user(difficulty)

    if is_list_equal(sequence, user_list):
        print('Congrats! You win')
    else:
        print('You LOSE!')

# play(difficulty)
