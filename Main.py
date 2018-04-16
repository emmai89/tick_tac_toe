import random
import os

def createArray():
    board = [8 for x in range(10)]
    for value in range(0,10):
        board[value] = value
    return board

def drawBoard(board):
    hangman =("""
                  1 | 2 | 3
                 ------------
                  4 | 5 | 6
                 ------------
                  7 | 8 | 9
                  """)
    for char in hangman:
        try:
            for value in range(0,10):
                if int(char) == value:
                    print (board[value], end='')
                else :
                    print ("", end='')
        except Exception as e:
            print(char, end='')


board = createArray()
move = "n"
while not move == "x" and not move == "o":
    drawBoard(board)
    move = input("\n\nenter x or o: ")

place = input("\n\nwhere do you want to place it? ")

board[int(place)] = move
drawBoard(board)
