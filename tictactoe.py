from pickle import FALSE
import random
import pygame
import sys

board = ["⠀","⠀","⠀"],["⠀","⠀","⠀"],["⠀","⠀","⠀"]
turns = 1
gameOver = False

def init():
    global turns
    global gameOver
    while gameOver != True:
        turns += 1
        prompt()
        if turns > 9:
            print(drawBoard())
            break
    drawBoard()
    match winner():
        case 0:
            print("Draw")
        case 1:
            print("Player 1 Wins")
        case 2:
            print("Player 1 Wins")
    return

def drawBoard():
    output = ""
    for i in range(len(board)):
        for j in range(len(board[i])):
            output += board[i][j]
            if j == len(board[i])-1:
                break;
            output += "|"
        if i != len(board[i])-1:
            output += "\n------\n"
    output +=  "\n"
    return output

def prompt():
    res = -1
    global turns
    if turns % 2 == 0:
        print(drawBoard())
        res = int(input("\nPlayer 1:"))
        move(res)
    else:
        print(drawBoard())
        res = int(input("\nPlayer 2:"))
        move(res)
    print("_____________________________________")

def move(pos):
    match pos:
        case 1:
            place(0,0)
        case 2:
            place(0,1)
        case 3:
            place(0,2)
        case 4:
            place(1,0)
        case 5:
            place(1,1)
        case 6:
            place(1,2)
        case 7:
            place(2,0)
        case 8:
            place(2,1)
        case 9:
            place(2,2)


def place(x,y):
    global turns
    global gameOver
    if (board[x][y] == "⠀"):
        if turns % 2 == 0:
            board[x][y] = "X"
        else:
            board[x][y] = "O"
    else:
        print("That space is already taken!")
        prompt()
    if winner() != 0:
        gameOver = True

def winner():
    output = 0;

    if match("X", "horizontal"):
        output = 1

    if match("Y", "horizontal"):
        output = 2

    if match("X", "vertical"):
        output = 1

    if match("Y", "vertical"):
        output = 2
    #diagonal
    if match("X", "diagonal"):
        output = 1

    if match("Y", "diagonal"):
        output = 2
    return(output)

def match(mark, axis):
    count = 0
    match axis:
        case "horizontal":
            count = 0
            for i in board:
                for j in i:
                    if j != mark:
                        break
                    count += 1
                    if count == 3:
                        return(True)
        case "vertical":
            count = 0
            for i in board:
                for j in range(len(i)):
                    if i[j] != mark:
                        break
                    count += 1
                    if count == 3:
                        return(True)
                    
        case "diagonal":
            count = 0
            for i in range(len(board)):
                if board[i][i] != mark:
                    break
                count += 1
                if count == 3:
                    return(True)
            count = 0
            for i in reversed(range(len(board))):
                j = len(board) - 1 - i
                t = board[j][i]
                if t == mark:
                    count += 1
                if count == 3:
                    return(True)

init()