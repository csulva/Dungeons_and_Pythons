# import necessary packages
import random
import time

# Define character class
class Char:
    def __init__(self, name, class_, full_health, health, mana, weapon, damage):
        self.name = name
        self.class_ = class_
        self.full_health = full_health
        self.health = health
        self.mana = mana
        self.weapon = weapon
        self.damage = damage

    def __str__(self):
        return f'Name: {self.name}, Class: {self.class_}, Health: {self.health}, Mana: {self.mana}, Weapon: {self.weapon}, Damage: {self.damage}'

    # Define battle function
    def battle(self, other):
        print(f'{self.name} fights {other.name}.')
        while self.health > 0 or other.health > 0:
            time.sleep(1)
            fight = input(f'Press enter to roll a six-sided die for {self.name}\'s damage: ')
            damage = random.randint(1, 6) * self.damage
            if self.mana >= 20:
                self.magic_attack(other)
            if fight == 'restore health'.lower():
                self.restore_health()
            if fight == 'restore mana'.lower():
                self.restore_mana()
            time.sleep(1)
            print(f'You dealt {damage} damage to {other.name}.')
            other.health -= damage
            print(f'{other.name}\'s health is now {other.health}')
            if other.health <= 0:
                time.sleep(1)
                print(f'You have defeated {other.name} with your {self.weapon}!')
                quit()
            time.sleep(1)
            opponent_fight = input(f'Press enter to roll a four-sided die for {other.name}\'s damage: ')
            opponent_damage = random.randint(1, 4) * other.damage
            time.sleep(1)
            print(f'{other.name} dealt {opponent_damage} damage to you!')
            self.health -= opponent_damage
            print(f'Your health is now at {self.health}')
            if self.health <= 0:
                print(f'{other.name} has defeated you. Try again...')
                quit()

    # Define magic attack with 20 mana or more
    def magic_attack(self, other):
        if self.mana >= 20:
            print('You used your magic attack to deal twice the amount of damage!')
            damage = random.randint(1, 6) * self.damage * 2
            self.mana -= 20
    # Define restore health
    def restore_health(self):
        self.health = self.full_health
        print(f'You\'ve been restored to full health: {self.full_health}')
    # Define restore mana
    def restore_mana(self):
        self.mana += 20
        print(f'You now have {self.mana} mana!')

# Define opponent class
class Monster:
    def __init__(self, name, type, health, damage):
        self.name = name
        self.type = type
        self.health = health
        self.damage = damage

    def __str__(self):
        return f'{self.name} is a {self.type}, with {self.health}, capable of {self.damage} damage.'


paladin = Char('Pally', 'Paladin', 100, 100, 0, 'sword', 5)
barbarian = Char('Barb_1', 'Barbarian', 120, 120, 0, 'axe', 6)
sorceress = Char('Sorc', 'Sorceress', 80, 80, 20, 'wand', 4)

drax = Monster('Drax', 'Dragon', 100, 5)
andy = Monster('Andy', 'Spider', 120, 4)
damien = Monster('Damien', 'Demon', 70, 8)

barbarian.battle(damien)
