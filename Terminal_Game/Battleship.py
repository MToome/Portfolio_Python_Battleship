import random

# Python Terminal Game

# Board
# Builds the board with O, but also shows [], " and ,
def build_board(dims):
    return [['O' for _ in range(dims)] for _ in range(dims)]

# Prints board, showing only O
def print_board(board):
    for row in board:
        # * will not show [], " and ,
        print(*row)

# Ship spawn
# Randomly generates sthe ship and randomly also chooses the orientation and location
def spawn_ship(dims):
    # Ship lenght is randomly selected between 1 and dims size
    ship_len = random.randint(1,dims)
    # Ship orientation is randomly selected between 0 and 1
    ship_orientation = random.randint(0,1)
    # Checks if the orientation is 0 then it generates the random location
    if ship_orientation == 0:
        # Selects the row for the ship randomly between 0 and inputed dims size - 1, then multyples it to 
        ship_row = [random.randint(0, dims-1)] * ship_len
        ship_col = random.randint(0, dims - ship_len)
        cor = list(zip(ship_row, range(ship_col, ship_col + ship_len)))
    else:
        ship_col = [random.randint(0, dims-1)]* ship_len
        ship_row = random.randint(0, dims - ship_len)
        cor = list(zip(range(ship_row, ship_row + ship_len), ship_col))
    return cor

#Guessing
#This is for guessing where the ship is, also their is exit function in it and breaking protection from entering letters or to high or low number.
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
#Changing the board, showing where have been shot and where the ship has been hit.
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

#Defining the board size
board_size = build_board(4)

#Starting message
#Prints something when starting the game
def start_message():
    print("Get ready for battle")
    print("Let's sink a ship!!!")

#This is function where all is but toghether
def main():
    start_message()
    #Prints the board previously defined
    b = board_size
    #Shows the board
    print_board(board_size)
    #Generats the ship
    cruiser = spawn_ship(len(board_size))  
    #Empty list where values are store after guessing
    guess_list = []
    #Game end is defined, if the ship lenght is 0 game ends, until then it cycles
    while len(cruiser) > 0:
        #calls the guessing function
        player_guess = player_shoot()
        #Changes the board and checking the ship location
        b = update(player_guess, b, cruiser, guess_list)
        #Shows the board
        print_board(board_size)
    #Prints after cycle has ended
    print("Congrats you sunk the ship")
    #Gives the valuse and ends the function
    return

main()