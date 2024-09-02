
def welcome():
    print(f'Hi {input("Enter your Username: ")} and welcome to the World of Games: The Epic Journey')

def start_play():
    games = ['Memory Game', 'Guess Game', 'Currency Roulette']
    while True:
        numbered_games= '\n'.join(f'{index + 1}. {game}' for index, game in enumerate(games))
        selection = input(f'Select Game (enter number 1-{len(games)}): \n{numbered_games}\n')
        if selection_validation(selection,games):
            break
        print("invalid input, try again")
        print('''\n\n\n------------\n\n\n''')
    difficulty = input('Enter disired difficulty (1-5): \n')

def selection_validation(selection, games):
    try:
        index = int(selection) - 1
        return 0 <= index < len(games)-1
    except ValueError:
        return False



