import random
import time
name = None
# Ask the player for their name.
name = input("Hello, what is your name? ")
# Display a message that greets them and introduces them to the game world.
intro = (f'Hello {name} welcome to the world of DnD. If at any point you get stuck, type "quit" to escape the dungeon.')
print(intro)
time.sleep(3)
# Present them with a choice between three doors.
set_of_options = set()
inventory_of_items = ['fists']

#functions
def go_back(choice):
    """[When go_back is initated, it takes you back
    to your original choices of doors]

    Args:
        choice ([string]): [If the choice complies, you will be taken to the next step]
    """
    if choice == 'exit' or choice == 'flee':
        choice = input(('You are back to the start.\nPick a door, right, left, or center: '))
        if choice == 'right':
            go_right(choice)
        if choice == 'left':
            go_left(choice)
        if choice == 'center':
            go_center(choice)

def go_right(choice):
    """[Examines the steps that occur when you choose the right room.]

    Args:
        choice ([string]): [The choice "right" comes from the input of the user which will allow this function to execute.]
    """
    if choice == 'right'.lower():
        choice = input(('You are now entering the right room.\nDo you want to explore or exit? '))
        if choice == 'exit'.lower():
            go_back(choice)
        if choice == 'explore'.lower():
            explore_right(choice)

def explore_right(choice):
    """[Examines the steps that occur when you *explore* the right room.]

    Args:
        choice ([string]): [If you type the next choice, it will take you to the next step.]
    """
    if choice == 'explore'.lower():
        time.sleep(1)
        print('Oh no, there is a dragon!')
        choice = input('Do you want to fight or flee? ')
        if choice == 'fight'.lower():
            print(f'You elect to try and fight the dragon with your {inventory_of_items[-1]}.')
            fight_dragon()
            quit()
        if choice == 'flee'.lower():
            go_back(choice)

def go_left(choice):
    """[Executes the steps that occur in the left room, either explore or exit.]

    Args:
        choice ([string]): [The choice "left" comes from the input of the user which will allow this function to execute.]
    """
    if choice == 'left'.lower():
        choice = input(('You are now entering the left room.\nDo you want to explore or exit? '))
    if choice == 'exit':
        go_back(choice)
    if choice == 'explore':
        explore_left(choice)

def explore_left(choice):
    """[Executes the steps that occur when you explore the left room.]

    Args:
        choice ([string]): [The choice "explore" comes from the input of the user which will give the next steps in the function.]
    """
    time.sleep(1)
    global inventory_of_items
    if choice == 'explore'.lower():
        print('You have found a sword!')
        inventory_of_items.append('sword')
        choice = input('Do you choose to explore or exit? ')
        if choice == 'exit'.lower():
            go_back(choice)
        if choice == 'explore'.lower():
            print('Oh no, you found a trap and were hit by a poisonous dart! You lose.')
            quit()

def go_center(choice):
    """[Executes the steps that occur when you enter the center room, to explore or exit the room.]

    Args:
        choice ([string]): [When the choice is "center" it will bring them to the center room.]
    """
    if choice == 'center'.lower():
        choice = input(('You are now entering the center room.\nDo you want to explore or exit? '))
    if choice == 'exit':
        go_back(choice)
    if choice == 'explore':
        choice = input('You see two doors, one left and one right. Which do you enter? ')
        if choice == 'right'.lower():
            print('You open the right door...')
            time.sleep(1.5)
            choice = input('Oh no, there\'s a temple guard! Do you fight or flee? ')
            if choice == 'fight':
                fight_temple_guard(choice)
            if choice == 'flee':
                go_center('center')
        if choice == 'left'.lower():
            left_door(choice)

def left_door(choice):
    """[This is the function for choosing the left door in the center room.]

    Args:
        choice ([string]): [the variable choice will be 'left' for how to enter the left door in the center room, and what comes next.]
    """
    if choice == 'left':
        print('You enter the left door...')
        time.sleep(1)
        print('You found an axe! ')
        inventory_of_items.append('axe')
        choice = input('Would you like to explore the other door or exit the center room? ')
        if choice == 'explore':
            print('You open the right door in the center room...')
            time.sleep(1.5)
            choice = input('Oh no, there\'s a temple guard! Do you fight or flee? ')
            if choice == 'fight':
                fight_temple_guard(choice)
            if choice == 'flee':
                go_center('center')
        if choice == 'exit':
            go_back(choice)

def fight_temple_guard(choice):
    """[When you fight the temple guard you encounter, it will allow you to roll to see if you beat him.
    Roll numbers are random and better chances if you have a weapon or not.]

    Args:
        choice ([string]): ['fight' string brings you to fight the temple guard and whatever comes next.]
    """
    global inventory_of_items
    if choice == 'fight':
        print(f'You elect to try and fight the temple guard with your {inventory_of_items[-1]}.')
        if 'sword' not in inventory_of_items and 'axe' not in inventory_of_items:
            choice = input('Press enter to roll a three-sided die: ')
            x = random.randint(1, 3)
            print(f"You rolled a {x}")
            choice = input("Press enter again to see the temple guard's roll: ")
            y = random.randint(1, 5)
            print(f"The temple guard rolled a {y}")
            if x > y:
                choice = input('Yay you killed the guard. Since he was guarding something, do you want to explore the temple or exit? ')
                if choice == 'explore':
                    explore_temple(choice)
                elif choice == 'exit'.lower():
                    choice = input('You exit the room. Do you want to explore the other room or exit? ')
                    if choice == 'exit':
                        go_back(choice)
                    else:
                        print('You decide to explore the other room in the center room...')
                        print('You enter the left door...')
                        time.sleep(1)
                        print('You found an axe! ')
                        inventory_of_items.append('axe')
                        choice = input('Would you like to explore the other door or exit the center room? ')
                        time.sleep(1)
                        if choice == 'explore':
                            print('You have already killed the temple guard so the room is open...\n')
                            time.sleep(1)
                            explore_temple(choice)                
            elif y > x:
                print("Oh no, the temple guard beat you and you lose all your items! Start over.")
            while x == y:
                choice = input("It's a draw, roll again: ")
                x = random.randint(1, 3)
                print(f"You rolled a {x}")
                choice = input("Press enter again to see the temple guard's roll: ")
                y = random.randint(1, 5)
                print(f"The temple guard rolled a {y}")
                if x > y:
                    choice = input(f'Yay you killed the temple guard with your {inventory_of_items[-1]}. Since he was guarding something, do you want to explore the temple or exit?')
                    if choice == 'explore':
                        explore_temple(choice)
                    elif choice == 'exit':
                        choice = input('You exit the room. Do you want to explore the other room or exit? ')
                        if choice == 'exit':
                            go_back(choice)
                        else:
                            print('You decide to explore the other room in the center room...')
                            print('You enter the left door...')
                            time.sleep(1)
                            print('You found an axe! ')
                            inventory_of_items.append('axe')
                            choice = input('Would you like to explore the other door or exit the center room? ')
                            time.sleep(1)
                            if choice == 'explore':
                                print('You have already killed the temple guard so the room is open...\n')
                                time.sleep(1)
                                explore_temple(choice)                
                elif y > x:
                    print("Oh no, the temple guard beat you and you lose all your items! Start over.")
                    inventory_of_items = ['fists']
                    quit()
            quit()
        if 'sword' in inventory_of_items or 'axe' in inventory_of_items:
            choice = input('Press enter to roll an 8-sided die: ')
            x = random.randint(1, 8)
            print(f"You rolled a {x}")
            choice = input("Press enter again to see the temple guard's roll: ")
            y = random.randint(1, 5)
            print(f"The temple guard rolled a {y}")
            if x > y:
                choice = input('Yay you killed the guard. Since he was guarding something, do you want to explore the temple or exit? ')
                if choice == 'explore':
                    explore_temple(choice)
                elif choice == 'exit':
                    go_center('center')
            elif y > x:
                print("Oh no, the temple guard beat you and you lose all your items! Start over.")
                inventory_of_items = ['fists']
                quit()
            else:
                choice = input("It's a draw, roll again: ")
                x = random.randint(1, 8)
                print(f"You rolled a {x}")
                choice = input("Press enter again to see the temple guard's roll: ")
                y = random.randint(1, 5)
                print(f"The temple guard rolled a {y}")
                if x > y:
                    choice = input(f'Yay you killed the temple guard with your {inventory_of_items[-1]}. Since he was guarding something, do you want to explore the temple or exit? ')
                    if choice == 'explore':
                        explore_temple(choice)
                    elif choice == 'exit':
                        choice = input('You exit the room. Do you want to explore the other room or exit? ')
                        if choice == 'exit':
                            go_back(choice)
                        else:
                            print('You decide to explore the other room in the center room...')
                            print('You enter the left door...')
                            time.sleep(1)
                            print('You found an axe! ')
                            inventory_of_items.append('axe')
                            choice = input('Would you like to explore the other door or exit the center room? ')
                            time.sleep(1)
                            if choice == 'explore':
                                print('You have already killed the temple guard so the room is open...\n')
                                time.sleep(1)
                                explore_temple(choice)     
                elif y > x:
                    print("Oh no, the temple guard beat you and you lose all your items! Start over.")
                    inventory_of_items = ['fists']
                    quit()

def explore_temple(choice):
    """[Allows you to execute the steps for exploring the temple if you kill the temple guard.
    You might win gold!]

    Args:
        choice ([string]): ['explore' is the string of the variable to allow you to explore the temple.]
    """
    if choice == 'explore'.lower():
        print('You explore the temple...')
        time.sleep(1.5)
        gold = random.randint(10, 100)
        print(f'You found {gold} pieces of gold! You win!')
        quit()

def fight_dragon():
    """[Similar to fighting the temple guard, except does not take an argument. You will fight the dragon
    with a random roll based on what weapons you have in your inventory.]
    """
    global inventory_of_items
    if 'sword' not in inventory_of_items and 'axe' not in inventory_of_items:
        choice = input('Press enter to roll a two-sided die: ')
        x = random.randint(1, 2)
        print(f"You rolled a {x}")
        choice = input("Press enter again to see the dragon's roll: ")
        y = random.randint(1, 6)
        print(f"The dragon rolled a {y}")
        if x > y:
            print(f'Yay you killed the dragon with your {inventory_of_items[-1]}. You win!')
        elif y > x:
            print("Oh no, the dragon beat you and you lose all your items! Start over.")
        while x == y:
            choice = input("It's a draw, roll again: ")
            x = random.randint(1, 2)
            print(f"You rolled a {x}")
            choice = input("Press enter again to see the dragon's roll: ")
            y = random.randint(1, 6)
            print(f"The dragon rolled a {y}")
            if x > y:
                print(f'Yay you killed the dragon with your {inventory_of_items[-1]}. You win!')
                quit()
            elif y > x:
                print("Oh no, the dragon beat you and you lose all your items! Start over.")
                inventory_of_items = ['fists']
                quit()
        quit()
    if 'sword' in inventory_of_items or 'axe' in inventory_of_items:
        choice = input('Press enter to roll an 8-sided die: ')
        x = random.randint(1, 8)
        print(f"You rolled a {x}")
        choice = input("Press enter again to see the dragon's roll: ")
        y = random.randint(1, 6)
        print(f"The dragon rolled a {y}")
        if x > y:
            print(f'Yay you killed the dragon with your {inventory_of_items[-1]}. You win!')
        elif y > x:
            print("Oh no, the dragon beat you and you lose all your items! Start over.")
            inventory_of_items = ['fists']
        else:
            choice = input("It's a draw, roll again: ")
            x = random.randint(1, 8)
            print(f"You rolled a {x}")
            choice = input("Press enter again to see the dragon's roll: ")
            y = random.randint(1, 6)
            print(f"The dragon rolled a {y}")
            if x > y:
                print(f'Yay you killed the dragon with your {inventory_of_items}. You win!')
                quit()
            elif y > x:
                print("Oh no, the dragon beat you and you lose all your items! Start over.")
                inventory_of_items = []
                quit()

while True:
# choice != 'quit'.lower():
    choice = input('Pick a door, right, left, or center: ').lower()
    try: 
        choice == choice
        if choice == 'right':
            go_right(choice)
            if choice == 'exit'.lower():
                go_back(choice)
        if choice == 'left':
            go_left(choice)
            if choice == 'exit'.lower():
                go_back(choice)
        if choice == 'center':
            go_center(choice)
        elif choice == 'quit'.lower():
            quit()
    except:
        print('Try again')
    else:
        print('Try again')
