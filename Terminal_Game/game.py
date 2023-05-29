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

show_board(9)

#Ship spawn
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
    print(list(cor))

ship = spawn_ship(3, 1, 2, 4); ship

