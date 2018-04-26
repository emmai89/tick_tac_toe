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
                    os.system('cls||clear')
                    print (place, " is taken")
            else :
                os.system('cls||clear')
                print ("no negative values is taken")
        except Exception as e:
            os.system('cls||clear')
            print("please enter a valid number")
    return place

def winMessage(player, board, scores):
    os.system('cls||clear')
    drawBoard(board)
    print("\n\n\t\t", player, " won!\n")
    if player == "x" :
        scores[0] += 1
    else :
        scores[1] += 1


def winning(board, scores):
    winner = False
    if board[1] == board[2] == board[3]:
        winner = True
        winMessage(board[1], board, scores)
    if board[4] == board[5] == board[6]:
        winMessage(board[5], board, scores)
        winner = True
    if board[7] == board[8] == board[9]:
        winMessage(board[8], board, scores)
        winner = True
    if board[1] == board[4] == board[7]:
        winMessage(board[4], board, scores)
        winner = True
    if board[8] == board[5] == board[2]:
        winMessage(board[5], board, scores)
        winner = True
    if board[3] == board[6] == board[9]:
        winMessage(board[6], board, scores)
        winner = True
    if board[9] == board[5] == board[1]:
        winMessage(board[5], board, scores)
        winner = True
    if board[3] == board[5] == board[7]:
        winMessage(board[5], board, scores)
        winner = True
    return winner

def begin(scores):
    board = createArray()
    winner = False
    round = 0
    while not winner:
        os.system('cls||clear')
        round += 1
        peice = validPiece(board, round)
        place = validPlace(board, peice)
        board[place] = peice
        winner = winning(board, scores)
        if round == 9 :
            drawBoard(board)
            print("\n\n\t\tIt's a draw")
            winner = True
