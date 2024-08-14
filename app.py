def welcome():
    print(f'Hi {input("Enter your Username: ")} and welcome to the World of Games: The Epic Journey')

def start_play():
    games = ['1. Memory Game', '2. Guess Game', '3. Currency Roulette']
    selection = games[int(input(f'Select Game (enter number 1-3): \n{", ".join(games)}\n')) - 1]
    difficulty = input('Enter disired difficulty (1-5): \n')