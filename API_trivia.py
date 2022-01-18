import requests
import time

trivia_url = 'https://opentdb.com/api.php?amount=1&category=16&type=boolean'
request = requests.get(trivia_url).json()
question = request['results'][0]['question']
answer = request['results'][0]['correct_answer']
def answer_trivia():
    print('In order to enter this room, you must correctly answer a board-game themed trivia question with either "True" or "False"...')
    time.sleep(1)
    trivia = input(f'{question} ')
    if trivia.capitalize() == answer:
        print('Correct! You may enter...')
        pass
    else:
        try_again = input('Incorrect! Would you like to try again? ').lower()
        if try_again == 'yes' or try_again == 'y':
            answer_trivia()
        else:
            pass

answer_trivia()