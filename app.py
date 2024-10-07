def welcome():
    print(f'Hi {input("Enter your Username: ")} and welcome to the World of Games: The Epic Journey')

selected_difficulty = None
def start_play():
    games = ['Memory Game', 'Guess Game', 'Currency Roulette']
    max_difficulty = 5
    numbered_games = '\n'.join(f'{index + 1}. {game}' for index, game in enumerate(games))
    selected_game = get_user_input_validate_with_message(len(games),
                                                         f'Select Game (enter number 1-{len(games)}): \n{numbered_games}\n')
    selected_difficulty = get_user_input_validate_with_message(max_difficulty, 'Enter disired difficulty (1-5): \n')


def number_validation(number, end_of_range):
    try:
        number = int(number)
        return number in range(1, end_of_range + 1)
    except ValueError:
        return False


def get_user_input_validate_with_message(end_of_range, message="Enter selection:\n"):
    while True:
        user_input = int(input(message))
        if number_validation(user_input, end_of_range):
            break
        print("invalid input, try again")
        print('''\n\n\n------------\n\n\n''')

    return int(user_input)
