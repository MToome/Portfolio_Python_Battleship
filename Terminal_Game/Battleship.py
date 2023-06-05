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
def spawn_ship(dims):
    ship_len = random.randint(1,dims)
    ship_orientation = random.randint(0,1)
    if ship_orientation == 0:
        ship_row = [random.randint(0, dims-1)] * ship_len
        ship_col = random.randint(0, dims - ship_len)
        cor = list(zip(ship_row, range(ship_col, ship_col + ship_len)))
    else:
        ship_col = [random.randint(0, dims-1)]* ship_len
        ship_row = random.randint(0, dims - ship_len)
        cor = list(zip(range(ship_row, ship_row + ship_len, ship_col)))
    return cor

#Guessing
def player_shoot():    
    while(True):
        shoot_col = input("Col: ") 
        if shoot_col == "exit":
            exit()
        try:
            int(shoot_col)
        except:
            print("Please enter a number without a decimel")
            continue
        if int(shoot_col) > len(board_size) or int(shoot_col) < 1:
            print("Please, enter number in the board.")
            continue
        else:
            break
    while(True):   
        shoot_row = input("Row:")
        if shoot_row.lower() == "exit":
            exit()
        try:
            int(shoot_row)
        except:
            print("Please enter a number without a decimel")
            continue
        if int(shoot_row) > len(board_size) or int(shoot_row) < 1:
            print("Please, enter number in the board.")
            continue
        else:
            break
    return (int(shoot_row)- 1, int(shoot_col) - 1)



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

board_size = build_board(4)

def start_message():
    print("Get ready for battle")
    print("Let's sink a ship!!!")

def main():
    start_message()
    b = board_size
    print_board(board_size)
    cruiser = spawn_ship(len(board_size))  
    guess_list = []
    while len(cruiser) > 0:
        player_guess = player_shoot()
        b = update(player_guess, b, cruiser, guess_list)
        print_board(board_size)
    print("Congrats you sunk the ship")
    game_continues = input("do you want to try again?")
    if game_continues.lower() == "yes":
        guess_list.clear()
        main()
    else:
        return

main()