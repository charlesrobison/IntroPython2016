#! /usr/bin/env python

"""

DICE ROLLER FOR ALL YOUR GAMING NEEDS!
This program will allow a user to pick from a number of dice types
and roll them individually, in multiples of the same dice, or as an assortment
of different dice.

"""

# Imports
import random


# Define Global Variables
dice_dict = {"1": [random.randint(1, 2)],
             "2": [random.randint(1, 4)],
             "3": [random.randint(1, 5)],
             "4": [random.randint(1, 6)],
             "5": [random.randint(1, 10)],
             "6": [random.randint(1, 12)],
             "7": [random.randint(1, 20)],
             "8": [random.randint(1, 100)]}

dice_list = ["d2", "d4", "d6", "d8", "d10", "d12", "d20", "d100"]

number_of_dice = [str(x) + '.' for x in range(1, len(dice_list) + 1)]

selection_list = []


# Define program functions
def main():
    print("Hi there and welcome to the Super Dice Roller!" '\n'
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


def roll_die():
    """ Roll dice function. Rolls matching die for every value in selection_list object. """
    die_roll_dict = {}
    for die in selection_list:
        if die in dice_dict:
            die_roll_dict[die] = dice_dict[die]
        print(die_roll_dict)
    # ToDo - generate different rand_int value for each roll


def die_amount_selector(user_input):
    """ Prompt user for amount of dice to roll and then add to selection list. """
    try:
        die_amount = int(input("How many would you like to roll? '\n> "))
    except ValueError:
        print("Please enter an appropriate value.")
        die_amount_selector(user_input)
    else:
        selection_list.extend((user_input.strip('.') * die_amount))
        print(selection_list)
        roll_more_prompt()


def roll_more_prompt():
    """ Check with user if they would like to roll more / different dice. """
    print("Would you like to roll any additional dice?")
    while True:
        confirm = input("Yes (y) or No (n)? '\n> ")
        if confirm == 'y':
            dice_menu()
        elif confirm == 'n':
            roll_die()


main()
