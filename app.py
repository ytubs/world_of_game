from memory_game import play as play_memory_game
from guess_game import play as play_guess_game
from currency_roulette_game import play as play_currency_roulette
from utils import get_user_input_validate_with_message

def welcome():
    print(f'Hi {input("Enter your Username: ")} and welcome to the World of Games: The Epic Journey')

# selected_difficulty = None
def start_play():
    games = ['Memory Game', 'Guess Game', 'Currency Roulette']
    max_difficulty = 5
    numbered_games = '\n'.join(f'{index + 1}. {game}' for index, game in enumerate(games))
    game_functions = {
        1 : play_memory_game,
        2 : play_guess_game,
        3 : play_currency_roulette,
    }
    selected_game_index = get_user_input_validate_with_message(len(games),
                                                         f'Select Game (enter number 1-{len(games)}): \n{numbered_games}\n') #held as int var from 1-3
    selected_difficulty = get_user_input_validate_with_message(max_difficulty, 'Enter disired difficulty (1-5): \n')
    game_functions[selected_game_index](selected_difficulty)





