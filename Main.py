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

def validPiece(board, round):
    move = round % 2
    peice = "x"
    if move == 1 :
        peice = "o"
    return peice

def validPlace(board, peice):
    notValid = True
    while notValid :
        drawBoard(board)
        try:
            print ("\n\n\t\t", peice, "'s move")
            userIn = input("\n\nwhere do you want to place it?")
            place = int(userIn)
            if place > 0 :
                if place == board[place] :
                    notValid = False
                else :
                    print (place, " is taken")
            else :
                print ("no negative values is taken")
        except Exception as e:
             print("please enter a valid number")
    return place

def winMessage(player):
    drawBoard(board)
    print("\n\n\t\t", player, " won!\n")


def winning(board):
    winner = False
    if board[1] == board[2] == board[3]:
        winMessage(board[1])
        winner = True
    if board[4] == board[5] == board[6]:
        winMessage(board[5])
        winner = True
    if board[7] == board[8] == board[9]:
        winMessage(board[8])
        winner = True
    if board[1] == board[4] == board[7]:
        winMessage(board[4])
        winner = True
    if board[8] == board[5] == board[2]:
        winMessage(board[5])
        winner = True
    if board[3] == board[6] == board[9]:
        winMessage(board[6])
        winner = True
    if board[9] == board[5] == board[1]:
        winMessage(board[5])
        winner = True
    if board[3] == board[5] == board[7]:
        winMessage(board[5])
        winner = True
    return winner

board = createArray()
winner = False
round = 0

while not winner:
    round += 1
    peice = validPiece(board, round)
    place = validPlace(board, peice)
    board[place] = peice
    winner = winning(board)
    if round == 9 :
        drawBoard(board)
        print("\n\n\t\tIt's a draw")
        winner = True
pass
