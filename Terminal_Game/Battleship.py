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
        # Selects the row for the ship randomly between 0 and inputed dims size - 1, then multyples it to ship length list
        ship_row = [random.randint(0, dims-1)] * ship_len
        # Pick the first cordinate for the ship, have to subtrack the ship lenght to make sure the ship would not go off board
        ship_col = random.randint(0, dims - ship_len)
        # Zip combines the ship_row and ship cord, list makes it to list 
        cor = list(zip(ship_row, range(ship_col, ship_col + ship_len)))
    # If the orientation is not 0 it will do the following
    else:
        # Selects the row for the ship randomly between 0 and inputed dims size - 1, then multyples it to ship length list
        ship_col = [random.randint(0, dims-1)]* ship_len
        # Pick the first cordinate for the ship, have to subtrack the ship lenght to make sure the ship would not go off board
        ship_row = random.randint(0, dims - ship_len)
        # Zip combines the ship_row and ship cord, list makes it to list
        cor = list(zip(range(ship_row, ship_row + ship_len), ship_col))
    # Returns the cordinates
    return cor

#Guessing
#This is for guessing where the ship is, also their is exit function in it and breaking protection from entering letters or to high or low number.
def player_shoot():    
    # As long as the value is True this loop will run
    while True:
        # User input is asked
        shoot_col = input("Col: ") 
        # If user input is "exit" it will end the game, .lower() is fail safe for if user has caps lock on
        if shoot_col.lower() == "exit" or shoot_col.lower() == "q":
            # Built in exit function
            exit()
        # This try helps to prevent game blowing up
        try:
            # Turns user input into integer
            int(shoot_col)
        # If try fails does this
        except:
            # Shows this
            print("Please enter a number without a decimel")
            # restarts the loop
            continue
        # When input is higher the board size or lower then 1 
        if int(shoot_col) > len(board_size) or int(shoot_col) < 1:
            # It shows this
            print("Please, enter number in the board.")
            # And restarts the loop
            continue
        # If the input will pass all failsafe
        else:
            # It ends the loop
            break
    # Same as shoot_col
    while True:   
        shoot_row = input("Row:")
        if shoot_row.lower() == "exit" or shoot_row.lower() == "q":
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
    # This ends the function and returns the input reduced by one because python starts counting at 0
    return (int(shoot_row)- 1, int(shoot_col) - 1)



#Updating
#Changing the board, showing where have been shot and where the ship has been hit.
def update(guess, board, ship, guess_list):
    # Checks if the guess player made is allready made and if it is
    if guess in guess_list:
        # it shows this text
        print("You allready shot their")
    # When player hits the ship
    elif guess in ship:
        # Shows this text
        print("Direct hit")
        # Enters X in the board
        board[guess[0]][guess[1]] = "X"
        # Removes the location from the ship list
        ship.remove(guess)
    # When if and elif is not triggered
    else:
        # Shows this text
        print("Missed")
        # Enters - to the board
        board[guess[0]][guess[1]] = "-"
        # Enters the guess to the guess_list
    guess_list.append(guess)
    # Ends the functin and returns the updated board
    return board

#Defining the board size
board_size = build_board(4)

# Starting message
# Prints something when starting the game
def start_message():
    print("Get ready for battle")
    print("Let's sink a ship!!!")

# This function combines it all
def main():
    while True:
        start_message()
        # Prints the board previously defined
        b = board_size
        # Shows the board
        print_board(board_size)
        # Generats the ship
        cruiser = spawn_ship(len(board_size))  
        # Empty list where values are store after guessing
        guess_list = []
        # Game end is defined, if the ship lenght is 0 game ends, until then it cycles
        while len(cruiser) > 0:
            # Calls the guessing function
            player_guess = player_shoot()
            # Changes the board and checking the ship location
            b = update(player_guess, b, cruiser, guess_list)
            # Shows the board
            print_board(board_size)
        # Prints after cycle has ended
        print("Congrats you sunk the ship")
        # Asks the player input if the player wants  to play again
        game_restart = input("Do you want to play again? y or n : ")
        # .lower() makes the ansewr lower case and the it checks if it is y
        if game_restart.lower() == "y":
            # If it is y loop will run as many times as their was guesses
            for i in range(len(guess_list)):
                # Num gets the valu of one guess, row and column
                num = guess_list[i]
                # This changes all the hits and miss markers to O, their would be a clean board again
                board_size[num[0]][num[1]] = "O"
            # Emptys the guess list
            guess_list.clear()
            # Starts the main function again
            continue
        # Ends the function
        return

# Calls the function
main()