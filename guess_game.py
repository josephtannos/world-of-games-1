import random


def guess_game(choose_game_difficulty):
    play(choose_game_difficulty)


def generate_number(choose_game_difficulty):
    return random.randint(1, choose_game_difficulty)


def get_guess_from_user(choose_game_difficulty):
    choose_game_difficulty = int(input(f"Please Choose a random number  from 1 to {choose_game_difficulty}: "))
    return choose_game_difficulty

def compare_result(secret_number, user_secret_number):
    if user_secret_number > secret_number:
        return True
    return False

def play(choose_game_difficulty):
    secret_number = generate_number(choose_game_difficulty)
    user_secret_number = get_guess_from_user(choose_game_difficulty)
    result = compare_result(secret_number, user_secret_number)
    if result:
        print('You Won!')
    else:
      print('You Lost!')
    print(f'your choice is {user_secret_number} and the pc choice is {secret_number}')


