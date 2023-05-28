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
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def show_board(size):
    header = []
    board  = [header]
    for i in range(size):
        header.append("    " + alphabet[i])
    for i in range(size):
        i += 1
        board.append(str(i) +("[ ]"*size))
    for row in board:
        print((" ").join(row))

show_board(9)

