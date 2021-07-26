# Ask the player for their name.
# Display a message that greets them and introduces them to the game world.
# Present them with a choice between two doors.
# If they choose the left door, they'll see an empty room.
# If they choose the right door, then they encounter a dragon.
# In both cases, they have the option to return to the previous room or interact further.
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
# When encountering the dragon, they have the choice to fight it.
# If they have the sword from the other room, then they will be able to defeat it and win the game.
# If they don't have the sword, then they will be eaten by the dragon and lose the game.

import random

name = None
name = input("Hello, what is your name? ")
intro = (f'Hello {name} welcome to the world of DnD. If at any point you get stuck, press ctrl+c to escape the dungeon.')
print(intro)
start_over = 'Pick a door, right, left, or center: '
choice = None
choice_1 = input('Pick a door, right, left, or center: ').lower()
set_of_options = set()
inventory_of_items = []

right = 'right'
left = 'left'
center = 'center'

left_room = set(['explore', 'exit'])
right_room = set(['explore', 'exit'])
center_room = set(['explore', 'exit'])
state = 'room'

while choice == None:
    if choice_1 == right:
        choice = input('You have chosen the right door... Do you explore or exit? ').lower()
        choice_1 = input('Pick a door, right, left, or center: ').lower()
        if choice == 'explore':
            print("Oh no, you've encountered a dragon!")
            choice = input('Would you like to fight or flee? ').lower()
            if choice == 'fight':
               if choice == 'fight':
                    choice = input('Press enter to roll a 6-sided die: ')
                    x = random.randint(1, 6)
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
                        x = random.randint(1, 6)
                        print(f"You rolled a {x}")
                        choice = input("Press enter again to see the dragon's roll: ")
                        y = random.randint(1, 6)
                        print(f"The dragon rolled a {y}")
                        if x > y:
                            print('Yay you killed the dragon with the sword. You win!')
                            break
                        elif y > x:
                            print("Oh no, the dragon beat you and you lose all your items! Start over.")
                            break
            elif choice == 'flee':
                print(intro)
        elif choice == 'exit':
            choice = choice_1
        else:
            print('Please enter your command: ')
    if choice_1 == "left":
        print('You have chosen the left door... It is dark.')
        choice = input('Do you explore or exit? ')
        if choice == 'explore':
            choice = input('Wow, you have found a sword. Now what? Stay here or exit the room? ')
            inventory_of_items.append('Sword')
            if choice == 'stay here' or choice == 'stay':
                print('OK have fun with your new sword.')                    
                break
            elif choice == 'exit' or choice == 'exit the room':
                choice_1 == right
                print(start_over)
#         choice_5 = input('Would you like to explore the right room or go through the center door? ')
        #         if choice_5 == 'y' or choice_5 == 'yes' or choice_5 == 'right':
        #             print('Now entering the room on the right\nOh no, there is a dragon.')
        #             choice_7 = input('Do you fight or flee? ')                    
        #             if choice_7 == 'fight':
        #                 choice_8 = input('Press enter to roll a 6-sided die: ')
        #                 x = random.randint(1, 6)
        #                 print(f"You rolled a {x}")
        #                 choice_9 = input("Press enter again to see the dragon's roll: ")
        #                 y = random.randint(1, 6)
        #                 print(f"The dragon rolled a {y}")
        #                 if x > y:
        #                     print('Yay you killed the dragon with the sword. You win!')
        #                 elif y > x:
        #                     print("Oh no, the dragon beat you! Try again next time...!")
        #                 while x == y:
        #                     choice_10 = input("It's a draw, roll again: ")
        #                     x = random.randint(1, 6)
        #                     print(f"You rolled a {x}")
        #                     choice_9 = input("Press enter again to see the dragon's roll: ")
        #                     y = random.randint(1, 6)
        #                     print(f"The dragon rolled a {y}")
        #                     if x > y:
        #                         print('Yay you killed the dragon with the sword. You win!')
        #                         break
        #                     elif y > x:
        #                         print("Oh no, the dragon beat you and you lose all your items! Start over.")
        #                         break
        #                 break
        #             elif choice_7 == 'flee':
        #                 print('Well then, you escaped the dragon, but not too heroicly...')
        #                 break
        #         elif choice_5 == 'n' or choice_5 == 'no':
        #             print('No? OK have fun with your new sword in the empty room.')
        #             break
        # elif choice_3 == 'exit' or choice_3 == 'exit the room':
        #     print(intro)
        #     choice = input('Pick a door, right or left: ')
    if choice_1 == "center" or choice_1 == "c" or choice_1 == "straight":
        pass


