import random
import time
import sys
import os

from app import get_user_input_validate_with_message


difficulty = 4
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

def clear_console():
    if 'PYCHARM_HOSTED' in os.environ:
        # If running in PyCharm
        print("\n" * 1000)  # Print 1000 new lines to "clear" the console, not ideal but works..
    else:
        # For other environments (like terminal)
        os.system('cls' if os.name == 'nt' else 'clear')

def clear_last_line():
    # Move the cursor up one line and clear that line
    print("\033[F\033[K", end='')
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
    # clear_last_line()
    clear_console()

    user_list = get_list_from_user(difficulty)

    if is_list_equal(sequence, user_list):
        print('Congrats! You win')
    else:
        print('You LOSE!')



# play(difficulty)




