"""
main to run game tree

generates combinations and places it in tree
will check for win conditions as well to stop filling the entire board
"""

from GameTree import GameTree
from collections import deque


def checkWin(self, board, player):
    # horizontal
    if board[0] == player and board[1] == player and board[2] == player:
        return 1
    if board[3] == player and board[4] == player and board[5] == player:
        return 1
    if board[6] == player and board[7] == player and board[8] == player:
        return 1

    # vertical
    if board[0] == player and board[3] == player and board[6] == player:
        return 1
    if board[1] == player and board[4] == player and board[7] == player:
        return 1
    if board[2] == player and board[5] == player and board[8] == player:
        return 1

    # diagonal
    if board[0] == player and board[4] == player and board[8] == player:
        return 1
    if board[2] == player and board[4] == player and board[6] == player:
        return 1

    return 0


def printBoard(self, arr):
    board = [' ', 'x', 'o']
    print(" %s | %s | %s" % (board[arr[0]], board[arr[1]], board[arr[2]]))
    print("---+---+---")
    print(" %s | %s | %s" % (board[arr[3]], board[arr[4]], board[arr[5]]))
    print("---+---+---")
    print(" %s | %s | %s" % (board[arr[6]], board[arr[7]], board[arr[8]]))
    print()


if __name__ == "__main__":

    gt = GameTree()

    # game board has 3 possibilities, empty, X or O
    pc = [' ', 'x', 'o']
    c = [0] * 9
    arr = [0] * 9

    gt.addRoot(arr)
    pos = 1

    # generate tic tac toe combination add in game tree
    for c[0] in range(3):
        for c[1] in range(3):
            for c[2] in range(3):
                for c[3] in range(3):
                    for c[4] in range(3):
                        for c[5] in range(3):
                            for c[6] in range(3):
                                for c[7] in range(3):
                                    for c[8] in range(3):
                                        countX = sum([1 for x in c if x == 1])
                                        countY = sum([1 for x in c if x == 2])
                                        if abs(countX - countY) < 2:
                                            if checkWin(c, 1) + checkWin(c, 2) == 1:
                                                arr = c
                                                gt.addChild(pos, arr)
                                                pos += 1

    myDeque = deque()
    print("Program start")
    print("What type of traversal do you want to use?")
    search = input("B = breath first, D = depth first")

    # tree traversal will be placed in a queue
    if search == 'B':
        myDeque = gt.breadthFirst()
    else:
        myDeque = gt.depthFirst()

    # loop that shows the first 9 items in tree then loops again
    text = input("press enter to start print")
    while text == "":
        for i in range(9):
            printBoard(myDeque.popleft())

        text = input("press enter to continue print")
