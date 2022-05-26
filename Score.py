import os

from Utils import SCORES_FILE_NAME


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r+') as f:
            current_score = f.readlines()[-1]
            current_score = int(current_score) if current_score != "" else 0
            new_value = points_of_winning + current_score
            f.write("\n" + str(new_value))

    else:
        with open(SCORES_FILE_NAME, 'w+') as f:
            f.write(str(points_of_winning))


def get_latest_score():
    score = ""
    if os.path.exists(SCORES_FILE_NAME):
       with open(SCORES_FILE_NAME, 'r') as f:
           score = str(f.readlines()[-1])
    return score
