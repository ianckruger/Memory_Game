""" Name:Ian Kruger
Date:4-22-2023
Assignment:Part C (memoryServices)
Pseudocode: None
"""

import random
from node import Node


class MemoryGame:
    """Description: This class is designed to function as a Memory Game
                Attributes:
                    num_pairs(int): --> Set to none to create default value of 6, amount of pairs of cards for the game
                    turns (int) --> tracks amount of user turns as a "score" or to end game if reachs max cards
                    cards(list) --> list of card nodes to function the game
                    maxTurn (int) --> default value of None, can be changed, ends game if turn == maxturns
                    message(str) --> stores message based on a win or loss for program to print
                Behaviors:
                    generateCards(num_pairs,cards) --> uses random.py to shuffle list of cards and store each value in a
                     node for class card list
                    displayCards()--> displays current board (self.cards)
                    playTurn()--> ask user for input to select cards
                    play()--> determines if there is max turn for game; if none, self.played; if so, breaks loop if
                    turns = max turns, calls playTurn
                    played()--> calls playTurn until game is finished, displays turns as "score"

        """
    num_pairs = None
    turns = 0
    cards = []
    maxTurn = None
    message = None

    def __init__(self, pairs=None):
        if pairs is None:
            pairs = 6
        self.num_pairs = pairs
        self.cards = []
        self.turns = 0
        self.generateCards()

    def setMaxTurn(self, max):
        self.maxTurn = max

    def getMaxTurn(self):
        return self.maxTurn

    def getTurns(self):
        return self.turns

    def setNumPairs(self, pair):
        self.num_pairs = pair

    def generateCards(self):
        """Description: This method is designed to create nodes based on randomized list values
                        Parameters:
                            none
                        Return:
                            updates self.cards with linked list of nodes
                """
        cards = list(range(1, self.num_pairs + 1)) * 2
        random.shuffle(cards)
        self.cards = [Node(value) for value in cards]

    def displayCards(self):
        """Description: This method is designed to display the board of cards with updated values of card node list
                                Parameters:
                                    none
                                Return:
                                    prints board
                        """
        print("Current board:")
        for card in self.cards:
            if card.found is False:
                print("*", end=" ")
            else:
                print(card.value, end=" ")
        print("\n")

    def playTurn(self):
        """Description: This method is designed to play the game for the program user, updates class turns, changes node
        values
                                Parameters:
                                    none
                                Return:
                                    updates found values of the linked list of nodes
                        """
        print(f"Turn: {self.turns + 1}")
        self.displayCards()
        print("Select first card:")
        while True:
            try:
                position1 = int(input(f"Enter card position (1-{len(self.cards)}): ")) - 1
                if position1 < 0 or position1 >= len(self.cards):
                    raise ValueError
                if self.cards[position1].found is True:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input or card already matched. Please enter a valid card position.")
        self.cards[position1].found = True
        self.displayCards()

        print("Select second card:")
        while True:
            try:
                position2 = int(input(f"Enter card position (1-{len(self.cards)}): ")) - 1
                if position2 < 0 or position2 >= len(self.cards) or position2 == position1:
                    raise ValueError
                if self.cards[position2].found is True:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input, card already matched, or same card selected. Please enter a valid card position.")
        self.cards[position2].found = True

        self.displayCards()
        if self.cards[position1].value == self.cards[position2].value:
            print("Match!")
            self.cards[position1].found = True
            self.cards[position2].found = True
        else:
            print("No match.")
            self.cards[position1].found = False
            self.cards[position2].found = False
        self.turns += 1

    def play(self):
        """Description: This method is designed to call the playTurn function after determining if there is a max turn
        limit
                                Parameters:
                                    none
                                Return:
                                    playTurn--> resets values if done
                        """
        if self.maxTurn is None:
            self.played()
        else:
            print("Welcome to Memory Game!")
            while True:
                self.playTurn()
                if all(card.found is True for card in self.cards):
                    print(f"Congratulations! You won in {self.turns} turns.\n")
                    self.message = "Good Job"
                    break
                if self.turns == self.maxTurn:
                    print("Out of turns... Unlucky :(\n")
                    self.message = "Nice Try!"
                    break

    def played(self):
        """Description: This method is designed to call play turn if there is no max turns
                                Parameters:
                                    none
                                Return:
                                    play turn--> resets values if done
                        """
        print("Welcome to Memory Game!")
        while True:
            self.playTurn()
            if all(card.found is True for card in self.cards):
                print(f"Congratulations! You won in {self.turns} turns.")
                # Resets the game
                for item in self.cards:
                    item.found = False
                self.turns = 0
                break


# User - can only play the game
# Administrator - can set parameters of game
# - can set amount of cards to memorize
# - can set max turns

