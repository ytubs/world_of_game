
import random
import requests

from app import selected_difficulty
from app import get_user_input_validate_with_message

random_usd = random.randint(1, 100)


def get_exchange_rate():
    """Retrieve the current exchange rate from USD to ILS."""
    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        data = response.json()
        # print(f"-------> CURRENT EXCHANGE RATE IS {data['rates']['ILS']}")
        return data['rates']['ILS']
    except Exception as e:
        print("Error fetching exchange rate:", e)
        return None

def get_money_interval():
    ils_value = random_usd * get_exchange_rate()
    upper_bound = int(round(ils_value + (10-selected_difficulty)))
    lower_bound = int(round(ils_value - (10-selected_difficulty)))
    return upper_bound,lower_bound





def get_guess_from_user():
    guess = get_user_input_validate_with_message(999,f'''The value is {random_usd} USD,
     guess how much is it in ILS! (input whole number)\n''')
    return guess


def compare_results():
    interval = get_money_interval()
    return interval[1] <= get_guess_from_user() <= interval[0]

def play():
    print('''Welcome to Currency Roulette!
    In this game, USD value of 1 - 100 is being pulled, your job is to guess it's value in ILS! good luck.''')
    if compare_results():
        print(f"You win! your guess is within the range!")
    else:
        print(f"you lose, cunt! ")

play()