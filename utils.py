import os

SCORES_FILE_NAME = 'Scores.txt'
BAD_RETURN_CODE = None


def screen_cleaner():
    if 'PYCHARM_HOSTED' in os.environ:
        # If running in PyCharm
        print("\n" * 1000)  # Print 1000 new lines to "clear" the console, not ideal but works..
    else:
        # For other environments (like terminal)
        os.system('cls' if os.name == 'nt' else 'clear')


def number_validation(number, end_of_range, start_of_range=1):
    try:
        number = int(number)
        return number in range(start_of_range, end_of_range + 1)
    except ValueError:
        return False


def get_user_input_validate_with_message(end_of_range, message="Enter selection:\n", error_message='invalid input, try again', start_of_range=1):
    while True:
        user_input = input(message)
        if number_validation(user_input, end_of_range, start_of_range):
            break
        print(f'\n{error_message}')
        print('''\n------------\n''')
    return int(user_input)