""" Name:Ian Kruger
Date:4-22-2023
Assignment:Part C (adminServices)
Pseudocode: None
"""
from memoryServices import MemoryGame


class Admin:
    """Description: This class is designed to function as a Memory Game
                    Attributes:
                        adminChoice(int)--> the choice of the admin from the menu
                        adminName(str)--> name of admin to make menu more friendly
                        game (object)--> instance of MemoryGame class
                    Behaviors:
                        printMenu()--> prints menu of choices for admin to continue the program
                        setMaxTurns()--> sets a max turn value for the memory game instance
                        setPairs()--> changes default pair of cards value for memory game instance
                        playMemory()--> plays the memory game from instance
                        exitSystem()--> exits the program
            """
    adminChoice = 0
    adminName = str
    game = MemoryGame

    def __init__(self, name: str, game=None):
        if game is None:
            game = MemoryGame()
        self.adminChoice = 0
        self.adminName = name
        self.game = game

    def setChoice(self, choice):
        self.adminChoice = choice

    def getChoice(self):
        return self.adminChoice

    def printMenu(self):
        """Description: This method is designed to print menu for admin to choose how program runs
                                        Parameters:
                                            none
                                        Return:
                                            self.playMemory or self.exitSystem or self.setMaxTurns or self.setPairs
                                """
        print(f"Welcome {self.adminName} to the Memory Game!")
        print("You have four choices.")
        print("1. Set the Max Turns.")
        print("2. Set the amount of pairs (default is 6).")
        print("3. Play.")
        print("4. Leave.")
        while True:
            try:
                decision = int(input("What do you choose? Enter a number: \n"))
                if not 0 < decision < 5:
                    raise ValueError
                self.setChoice(decision)
                break
            except ValueError:
                print("Please only enter 1-4.")
        if self.adminChoice == 1:
            self.setMaxTurns()
        elif self.adminChoice == 2:
            self.setPairs()
        elif self.adminChoice == 3:
            self.playMemory()
        elif self.adminChoice == 4:
            self.exitSystem()

    def setMaxTurns(self):
        """Description: This method is designed to update max turns of the game instance
                                        Parameters:
                                            maxT(int)--> called in function
                                        Return:
                                            printMenu after updated value
                                """
        try:
            maxT = int(input("What is the max amount of turns you want for the game?"))
            self.game.setMaxTurn(maxT)
        except ValueError:
            print("Please enter a number. Select option in menu to try again.")
        print(f"The maximum amount of turns is now {self.game.maxTurn}.\n")
        self.printMenu()

    def setPairs(self):
        """Description: This method is designed to update card pairs of the game instance
                                                Parameters:
                                                    pairs(int)--> called in function
                                                Return:
                                                    printMenu after updated value
                                        """
        try:
            pairs = int(input("How many pairs of cards would you like to play?: "))
            self.game.setNumPairs(pairs)
        except ValueError:
            print("Please enter an number. Select option in menu to try again.")
        self.game.generateCards()
        print(f"Amount of pairs is now {self.game.num_pairs}.\n")
        self.printMenu()

    def playMemory(self):
        """Description: This method is designed to call play function from MemoryGame instance
                                                Parameters:
                                                    none
                                                Return:
                                                    printMenu
                                        """
        self.game.play()
        print(f"{self.game.message}! Reloading menu...")
        self.printMenu()

    def exitSystem(self):
        """Description: This method is designed to end the program
                                                Parameters:
                                                    none
                                                Return:
                                                    print statement as goodbye message
                                        """
        print("You have chosen to exit the system.")
        print("Goodbye!")



