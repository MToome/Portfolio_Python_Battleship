import random

#Python Terminal Game

#player1 = input("Player 1 enter your name: ")
#player2 = input("Player 2 enter your name: ")

#Ship names
carrier = 5
battleship = 4
destroyer = 3
submarine = 3
patrol_boat = 2

#Board
def show_board(size):
    
    header = []
    board  = [header]
    for i in range(size):
        header.append("    " + str(i+1))
    for i in range(size):
        board.append(str(i+1) +("[ ]"*size))
    for row in board:
        print((" ").join(row))

#Testing Board function
#show_board(9)

#Ship spawn
"""
For multiplayer
def spawn_ship(size, orientation, row, col):
    ship_len = size
    ship_orientation = orientation
    if ship_orientation == 0:
        ship_row = [row-1]*size
        ship_col = (col-1)
        col_range = list(range(ship_col,ship_col + ship_len))
        cor = tuple(zip(ship_row, col_range))
    else:
        ship_col = [col-1]*size
        ship_row = (row-1)
        row_range = list(range(ship_row,ship_row + ship_len))
        cor = tuple(zip(ship_col, row_range))
    return list(cor)
"""
def spawn_ship(size):
    ship_len = random.randint(1,size)
    ship_orientation = random.randint(0,1)
    if ship_orientation == 0:
        ship_row = [random.randint(0, size-1)]*size
        ship_col = random.randint(0, size - ship_len)
        col_range = list(range(ship_col,ship_col + ship_len))
        cor = tuple(zip(ship_row, col_range))
    else:
        ship_col = [random.randint(0, size-1)]*size
        ship_row = random.randint(0, size - ship_len)
        row_range = list(range(ship_row,ship_row + ship_len))
        cor = tuple(zip(ship_col, row_range))
    return list(cor)


#Testing Ship spawning function 
#cruiser = spawn_ship(3)

#Guessing
def player_guess():    
    guess_col = int(input("Col: ")) - 1
    guess_row = int(input("Row:")) - 1
    return guess_col, guess_row


