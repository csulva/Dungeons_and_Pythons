# API Trivia
# Add to Command Line Game if desired

# Imports
import requests
import time

# Gather info from the API link
# The link provides a new question and answer at random
trivia_url = 'https://opentdb.com/api.php?amount=1&category=16&type=boolean'
request = requests.get(trivia_url).json()
question = request['results'][0]['question']
answer = request['results'][0]['correct_answer']

# Answer the trivia
def answer_trivia():
    """This function allows you to generate a random trivia question from the API and try to
    answer it in the command line. Questions I've selected are either True or False. To incorporate
    the function in your game, simply import the function and place it in the right place.
    If the user answers correctly, they go one way, else they go the other way, or however
    you desire the results to be.
    """
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

# Run the function to answer trivia
answer_trivia()