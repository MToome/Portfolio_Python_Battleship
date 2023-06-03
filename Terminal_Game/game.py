import random

#Python Terminal Game

#player1 = input("Player 1 enter your name: ")
#player2 = input("Player 2 enter your name: ")

"""
Ship names
carrier = 5
battleship = 4
destroyer = 3
submarine = 3
patrol_boat = 2
"""

#Board
"""
def show_board(size):
    header = []
    board  = [header]
    for i in range(size):
        header.append("    " + str(i+1))
    for i in range(size):
        board.append(str(i+1) +("[ ]"*size))
    for row in board:
        print((" ").join(row))
"""
def build_board(dims):
    return [['O' for _ in range(dims)] for _ in range(dims)]

def print_board(board):
    for row in board:
        print(*row)

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
def spawn_ship(size, dims):
    ship_len = random.randint(1,size)
    ship_orientation = random.randint(0,1)
    if ship_orientation == 0:
        ship_row = [random.randint(0, dims-1)] * ship_len
        ship_col = random.randint(0, dims - ship_len)
        cor = list(zip(ship_row, range(ship_col, ship_col + ship_len)))
    else:
        ship_col = [random.randint(0, dims-1)]* ship_len
        ship_row = random.randint(0, size - ship_len)
        cor = list(zip(ship_col, range(ship_row, ship_row + ship_len)))
    return cor

#Guessing
def player_shoot():    
    shoot_col = int(input("Col: ")) - 1
    shoot_row = int(input("Row:")) - 1
    return [shoot_row, shoot_col]



#Updating
def update(guess, board, ship, guess_list):
    if guess in guess_list:
        print("You allready shot their")
    elif guess in ship:
        print("Direct hit")
        board[guess[0]][guess[1]] = "X"
        ship.remove(guess)
    else:
        print("Missed")
        board[guess[0]][guess[1]] = "-"
        guess_list.append(guess)
    return board

board_size = build_board(9)
print_board(board_size)

cruiser = spawn_ship(3, len(board_size))    

guess_list = []
player_guess = player_shoot()
board_size = update(player_guess, board_size, cruiser, guess_list)
print_board(board_size)

