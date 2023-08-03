""" Name:Ian Kruger
Date:4-22-2023
Assignment:Part C (node)
Pseudocode: None
"""


class Node:
    """Description: This class is designed to function as a Memory Game
                    Attributes:
                        value(int)--> value of the node
                        next(object)--> next node in list
                        found(bool)--> if the cards is True its been found and disabled if false its still active
                    Methods:
                        none
            """
    value = int

    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.found = False

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def getFound(self):
        return self.found

    def setValue(self, value: int):
        self.value = value

    def setNext(self, nextNode):
        self.next = nextNode

    def setFound(self, found: bool):
        self.found = found
