from currrency_roulette_game import currency_roulette_game
from guess_game import guess_game
from memory_game import memory_game


def welcome(name):
    return print(f'Hello {name} and welcome to the World of Games (WoG).\n'
                 f'Here you can find many cool games to play.\n')

def load_game():
    choose_game_index = int(input("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n"
                              "2. Guess Game - guess a number and see if you chose like the computer.\n"
                              "3. Currency Roulette - try and guess the value of a random amount of USD in ILS.\n"
                              "Please choose a game to play: "))

    choose_game_difficulty = int(input("Please Choose game difficulty from 1 to 5: "))

    print(f"Game Index is {choose_game_index}, Game difficulty is {choose_game_difficulty}")

    if choose_game_index == 1:
        memory_game(choose_game_difficulty)
    elif choose_game_index == 2:
        guess_game(choose_game_difficulty)
    elif choose_game_index == 3:
        currency_roulette_game(choose_game_difficulty)
    else:
        print(f"Game with index {choose_game_index} is not found, please choose from 1-3")

