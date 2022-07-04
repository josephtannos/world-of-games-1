FROM python:3

WORKDIR /usr/src/app
ADD . /usr/src/app
ADD ./requirements.txt /requirements.txt
COPY ./Scores.txt .

ENV PYTHONPATH="$PYTHONPATH:/usr/src/app/venv"
RUN pip install -r /requirements.txt
EXPOSE 5000
CMD [ "python", "./MainScores.py" ]