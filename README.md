# Dungeons_and_Pythons
Dungeons and Pythons is an adventure game you can play on command line.

## Play the game
Welcome to Dungeons and Pythons! Battle monsters and collect items in this adventure-based game created to be played on the command line. Simply follow the steps by typing your responses to move through the game. Type "quit" or click "Run" to reset the game.
Play on [Repl.it](https://replit.com/@ChrisSulva/CommandLineGame#.replit){:target="_blank"}.
When you open the link, click "Run" as many times as you want to play.

## Other features

The file "dungeons_and_apis.py" is exactly the same as the command-line game above, but it uses the requests package to access the Uzby API and randomize your name based on the name you provide in the command line when you run the file.

If you want to try using a trivia game to integrate into your command-line game, you can find that information in the file: "api_trivia.py". Here, it will show you how to connect to the "Open Trivia Database" to randomize a question/answer pair and try to solve it on the command line. For my trivia category, I selected "Entertainment: Board Games".

I've also created a command-line game with classes that can battle each other based on their "classes" as seen in the "battle_classes.py" file. You can play this game on [Repl.it](https://replit.com/@ChrisSulva/CommandLineGamewithClasses#main.py) as well. To do so, simply pick two characters (variables) at the bottom and type *character1*.battle(*character2*) and click "Run" to initiate battle between the two classes. You will roll die for each until one loses all their health.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requests to integrate API data.

```bash
pip install requests
```
You may also want to do this in a virtual environment.

## Usage

```python
import requests

# returns 'random name generated from Uzby API'
request = requests.get(url)

# returns 'random trivia question from Open Trivia Database API'
request = requests.get(trivia_url).json()

import time

# the Terminal will pause for however many seconds you specify
time.sleep(3)

import random

# Returns random integer from the range you specify
gold = random.randint(10, 100)

```
## Contributing
Pull requests are welcome as I'd love to continue adding to the game(s) and diving deeper into the story. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## References
[CodingNomads Python Course](https://codingnomads.co/career-track/professional-python-web-development-course)

[Open Trivia Database](https://opentdb.com/)

[Uzby API](https://uzby.com/api) for randomizing names