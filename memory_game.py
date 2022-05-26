import random
import time


def memory_game(choose_game_difficulty):
    play(choose_game_difficulty)


def generate_sequence(choose_game_difficulty):
    random_numbers_list = []
    for i in range(choose_game_difficulty):
        random_numbers_list.append(random.randint(1, 101))
    return random_numbers_list


def get_list_from_user(choose_game_difficulty):
    user_numbers_list = []
    print('Please build a list of the numbers you saw')
    for i in range(choose_game_difficulty):
        random_input = int(input())
        user_numbers_list.append(random_input)
    return user_numbers_list

def is_list_equal(user_numbers_list, random_numbers_list):
    return user_numbers_list == random_numbers_list

def play(choose_game_difficulty):
    random_numbers_list = generate_sequence(choose_game_difficulty)
    print(random_numbers_list)
    time.sleep(1)
    print("\n" * 100)
    user_numbers_list = get_list_from_user(choose_game_difficulty)
    print(len(user_numbers_list))
    print(user_numbers_list)
    result = is_list_equal(user_numbers_list, random_numbers_list)
    if result:
        print('you won!')
    else:
        print('you lost!')
    print(f'your list is {random_numbers_list} and the user list is {user_numbers_list}')