
from flask import Flask, render_template

from Score import get_latest_score

app = Flask(__name__)


@app.route('/')
def index():
    score = get_latest_score()
    # TODO for some reason Score.txt is not found although it is and it's failing to read the latest value
    score = 10
    print(f'score is {score}')
    if score == "":
        return render_template('badIndex.html')
    return render_template('index.html', score=score)


if __name__ == '__main__':
    app.run()