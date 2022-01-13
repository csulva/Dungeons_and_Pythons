# Command_Line_Game
Adventure game you can play on command line

## Play the game
Play on [Repl.it](https://replit.com/@ChrisSulva/CommandLineGame#.replit)

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

## References
[CodingNomads Python Course](https://codingnomads.co/career-track/professional-python-web-development-course)
