""" Name:Ian Kruger
Date:4-22-2023
Assignment:Part C (userServices)
Pseudocode: None
"""
from memoryServices import MemoryGame


class User:
    """Description: This class is designed to function as a Memory Game
                        Attributes:
                            userChoice(int)--> the choice of the user from the menu
                            userName(str)--> name of user to make menu more friendly
                            game (object)--> instance of MemoryGame class
                        Behaviors:
                            printMenu()--> prints menu of choices for user to continue the program
                            playMemory()--> plays the memory game from instance
                            exitSystem()--> exits the program
                """
    userChoice = 0
    userName = str
    game = MemoryGame

    def __init__(self, name: str,game=None):
        if game is None:
            game = MemoryGame()
        self.game = game
        self.userChoice = 0
        self.userName = name

    def setChoice(self, choice):
        self.userChoice = choice

    def getChoice(self):
        return self.userChoice

    def printMenu(self):
        """Description: This method is designed to print menu for user to choose how program runs
                                Parameters:
                                    none
                                Return:
                                    self.playMemory or self.exitSystem
                        """
        print(f"Welcome {self.userName} to the Memory Game!")
        print("You have two choices.")
        print("1. Play")
        print("2. Leave")
        while True:
            try:
                decision = int(input("What do you choose? Enter a number: "))
                if not 0 < decision < 3:
                    raise ValueError
                self.setChoice(decision)
                break
            except ValueError:
                print("Please only enter 1 or 2.")
        if self.userChoice == 1:
            self.playMemory()
        elif self.userChoice == 2:
            self.exitSystem()

    def playMemory(self):
        """Description: This method is designed to call play function from MemoryGame instance
                                        Parameters:
                                            none
                                        Return:
                                            self.game.play() until they choose to exit the system
                                """
        self.game.play()
        while True:
            try:
                playAgain = input(f"{self.game.message}! Enter Y to play again. If you want to exit, enter any other "
                                  f"character: ")
                if playAgain == "Y":
                    self.game.play()
                else:
                    self.exitSystem()
                    break
            except ValueError:
                print("Please only enter the correct option.")

    def exitSystem(self):
        """Description: This method is designed to end the program
                                        Parameters:
                                            none
                                        Return:
                                            print statement as goodbye message
                                """
        print("You have chosen to exit the system.")
        print("Goodbye!")



