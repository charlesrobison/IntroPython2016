#! /usr/bin/env python3

"""

DICE ROLLER FOR ALL YOUR GAMING NEEDS!
This program will allow a user to pick from a number of dice types
and roll them individually, in multiples of the same dice, or as an assortment
of different dice.

"""

# Imports
import random
import tabulate
import numpy


# Define Global Variables
""" Dict object that takes user input (keys) and matches it with the side (value). """

side_dict = {"1": random.randint(1, 2),
             "2": random.randint(1, 4),
             "3": random.randint(1, 6),
             "4": random.randint(1, 8),
             "5": random.randint(1, 10),
             "6": random.randint(1, 12),
             "7": random.randint(1, 20),
             "8": random.randint(1, 100)}

""" List objects that are used to generate menu in dice_menu. """

dice_list = ["d2", "d4", "d6", "d8", "d10", "d12", "d20", "d100"]

number_of_dice = [str(x) + '.' for x in range(1, len(dice_list) + 1)]


# Classes
class Dice(object):

    def __init__(self, side=None, number=0, selection_list=None):
        self.side = side
        self.number = number
        self.selection_list = []
        if selection_list:
            self.selection_list.append(selection_list)

    def add_dice(self, side, number):
        """ Add selected number of dice to selection list object. """
        self.selection_list.extend(number * side)

    # def roll_dice_value(self):
    #     """ Returns random value for each die selected
    #      and then updates it to the die_roll_dict object for printing later. """
    #     die_roll_dict = {selected_die: []}
    #     for die in self.selection_list:
    #         print(die)
    #         die_roll_dict[die].append(self.side)
    #     # for die in self.selection_list:
    #     #     if die in side_dict.keys():
    #     #         die_roll_dict[die] = random.randint(1, side_dict[self.side])
    #     print(die_roll_dict.items())
    # ToDo - Fix roll_dice_value function

# Functions for main program
def main():
    print("Hail Champion and welcome to the Super Dice Roller!" '\n'
          "Please choose a dice to roll from the menu below, and then follow any additional instructions." '\n'
          "You'll be able to choose more and/or different dice afterwards.")
    dice_menu()


def dice_menu():
    """ Print out menu of dice options. """
    dice_options = zip(number_of_dice, dice_list)
    for number, dice in dice_options:
        print(number, dice)
    while True:
        user_input = input("> ") + '.'
        if user_input not in number_of_dice:
            print("Please try again.")
        else:
            die_amount_selector(user_input)


def die_amount_selector(user_input):
    """ Prompt user for amount of dice to roll and then add to selection_list object. """
    d = Dice()
    try:
        die_amount = int(input("How many would you like to roll? '\n> "))
    except ValueError:
        print("Please enter an appropriate value.")
        die_amount_selector(user_input)
    else:
        d.side = user_input.strip('.')
        d.number = die_amount
        d.add_dice(side=user_input.strip('.'), number=die_amount)
        roll_more_prompt(d)


def roll_more_prompt(d):
    """ Check with user if they would like to roll more / different dice. """
    print("Would you like to roll any additional dice?")
    while True:
        confirm = input("Yes (y) or No (n)? '\n> ")
        if confirm == 'y':
            dice_menu()
        elif confirm == 'n':
            print(d.selection_list)
            d.roll_dice_value()
            # ToDo - Include print die results function here


def print_die_results(d):
    """ Print contents of dice_roll_dict to a nice report. """
    print(tabulate.tabulate(d.get_dice_value(), headers="keys", tablefmt="fancy_grid", numalign="center"))

if __name__ == '__main__':
    main()
