""" Dice Rolling Simulator """

import random
import sys

def dice():
    """ dice rolling func """
    # asking user for num of dice + num of sides
    user_input_dice = input("How many dice's would you like to roll? ")
    user_input_sides = input("How many sides for each dice? ")
    # initializing empty array
    num_dice = []
    # for loop
    for i in range(int(user_input_dice)):
        num_dice.append(random.randint(1,int(user_input_sides)))
    
    return num_dice
    #dice3 = random.randint(1,6)
    #dice2 = random.randint(1,6)
    #print('First Die: ' + str(dice3) + '\nSecond Die: ' + str(dice2))

if __name__ == '__main__':
    print(dice())
