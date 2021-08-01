# Ask the player for their name.
# Display a message that greets them and introduces them to the game world.
# Present them with a choice between three doors.
# In both cases, they have the option to return to the previous room or interact further.
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
# When encountering the dragon, they have the choice to fight it.
# If they have the sword from the other room, then they will be able to defeat it and win the game.
# If they don't have the sword, then they will be eaten by the dragon and lose the game.
import random
name = None
name = input("Hello, what is your name? ")
intro = (f'Hello {name} welcome to the world of DnD. If at any point you get stuck, type "quit" to escape the dungeon.')
print(intro)
choice = input('Pick a door, right, left, or center: ').lower()
set_of_options = set()
inventory_of_items = ['fists']

#functions
def fight_dragon():
    global inventory_of_items
    if 'sword' and 'axe' not in inventory_of_items:
        choice = input('Press enter to roll a two-sided die: ')
        x = random.randint(1, 2)
        print(f"You rolled a {x}")
        choice = input("Press enter again to see the dragon's roll: ")
        y = random.randint(1, 6)
        print(f"The dragon rolled a {y}")
        if x > y:
            print('Yay you killed the dragon. You win!')
        elif y > x:
            print("Oh no, the dragon beat you and you lose all your items! Start over.")
        else:
            choice = input("It's a draw, roll again: ")
            x = random.randint(1, 2)
            print(f"You rolled a {x}")
            choice = input("Press enter again to see the dragon's roll: ")
            y = random.randint(1, 6)
            print(f"The dragon rolled a {y}")
            if x > y:
                print('Yay you killed the dragon with the sword. You win!')
                quit()
            elif y > x:
                print("Oh no, the dragon beat you and you lose all your items! Start over.")
                inventory_of_items = []
                print(inventory_of_items)
                quit()
        quit()
    if 'sword' or 'axe' in inventory_of_items:
        choice = input('Press enter to roll an 8-sided die: ')
        x = random.randint(1, 8)
        print(f"You rolled a {x}")
        choice = input("Press enter again to see the dragon's roll: ")
        y = random.randint(1, 6)
        print(f"The dragon rolled a {y}")
        if x > y:
            print('Yay you killed the dragon. You win!')
        elif y > x:
            print("Oh no, the dragon beat you and you lose all your items! Start over.")
        else:
            choice = input("It's a draw, roll again: ")
            x = random.randint(1, 8)
            print(f"You rolled a {x}")
            choice = input("Press enter again to see the dragon's roll: ")
            y = random.randint(1, 6)
            print(f"The dragon rolled a {y}")
            if x > y:
                print('Yay you killed the dragon with the sword. You win!')
                quit()
            elif y > x:
                print("Oh no, the dragon beat you and you lose all your items! Start over.")
                inventory_of_items = []
                print(inventory_of_items)
                quit()

def go_back(choice):
    if choice == 'exit':
        choice = input(('You are back to the start.\nPick a door, right left, or center: '))

def explore_right(choice):
    if choice == 'explore':
        print('Oh no, there is a dragon!')
        choice = input('Do you want to fight or flee? ')
        if choice == 'fight':
            print(f'You elect to try and fight the dragon with {inventory_of_items[-1]}.')
            fight_dragon()
            quit()

def go_right(choice):
    if choice == 'right':
        choice = input(('You are now entering the right room.\nDo you want to explore or exit? '))
        if choice == 'exit':
            go_back(choice)
        if choice == 'explore':
            explore_right(choice)


while choice != 'quit'.lower():
    choice == choice
    if choice == 'right':
        (go_right(choice))

