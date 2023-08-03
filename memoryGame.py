''' Name:Ian Kruger
Date:4-22-2023
Assignment:Part C (memoryGame)
Pseudocode:
# System of inheritance class
# Parent Class is MemoryGame; user or admin can inherit the user class.
# the admin and user class depend on the memory class, and the memory class depends on the linked list class for nodes

# I - Input
ask for name
print menu for choice between admin and user
create instance based on choice
if admin:
program = Admin()
# Prints a menu with 4 options
    Set max turns for game
    set number of pairs
    play
    exit
# Ask the user what option they would like
# Use a try-except to making sure they choose a valid option
copy process for user but only play and exit


# P - Process
call methods from memory class based on user or admin class
create set of cards
    each card has node value
    each card is linked to each other through a linked list
play the game
display board
user flips card
show card
choose another card
disable card values if properly chosen
else flip cards back over
    if all card values disabled game ends
    if all card values are not disable before max turn game ends




# O - Output
if user plays:
ask user if they want to play again
if they say no exit the program

if admin plays:
reprint menu
repeat process till user exits program
'''

from userServices import User
from adminServices import Admin


def chooseWay(name):
    """Description: This method is designed to determine if program user is user or admin
                            Parameters:
                                name --> put into user or admin instance
                            Return:
                                programC--> instance variable based on choice
                    """
    name = name
    print("--Menu--")
    print("Please choose one of the following...")
    print("1.User\n2.Admin")
    while True:
        try:
            choice = int(input("Please type 1 or 2 for your choice: "))
            if choice > 2 or choice < 1:
                raise ValueError
            if choice == 1:
                programC = User(name)
                break
            elif choice == 2:
                programC = Admin(name)
                break
        except ValueError:
            print("Please choose 1 or 2.")
    return programC


name = input("Hello! What is your name?: ")
try:
    programChoice = chooseWay(name)
    programChoice.printMenu()
except ValueError:
    print("You failed to follow instructions. Restart program and try again.")

