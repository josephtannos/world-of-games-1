import random
import datetime

from forex_python.converter import CurrencyRates

from Score import add_score


def currency_roulette_game(choose_game_difficulty):
     play(choose_game_difficulty)

def get_money_interval(choose_game_difficulty, random_amount):
    currency_rate = CurrencyRates()
    # when using latest date I get the following error ( USD TO ILS is not available for latest date)
    dt = datetime.datetime(2020, 3, 27, 11, 21, 13, 114505)
    usd_to_ils = currency_rate.get_rate('USD', 'ILS', dt)
    t = random_amount * usd_to_ils
    min_interval = t - (5 - choose_game_difficulty)
    max_interval = t + (5 + choose_game_difficulty)
    return min_interval, max_interval

def get_guess_from_user(random_amount):
    guess = float(input(f"How much is {random_amount}$ in ILS?"))
    return guess


def play(choose_game_difficulty):
    random_amount = random.randint(1, 101)
    min_interval, max_interval = get_money_interval(choose_game_difficulty, random_amount)
    guess = get_guess_from_user(random_amount)
    if guess <= max_interval and guess >= min_interval:
        print('You Won')
        add_score(choose_game_difficulty)
    else:
        print('You lost')
    print(f'your guess is {guess}, min interval is {min_interval}, max interval is {max_interval}')
