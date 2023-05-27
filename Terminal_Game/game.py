#Python Terminal Game

#player1 = input("Player 1 enter your name: ")
#player2 = input("Player 2 enter your name: ")

carrier = 5
battleship = 4
destroyer = 3
submarine = 3
patrol_boat = 2

board = ["""
 A   B   C   D   E   F
"""]


for i in range(6):
    i += 1
    board.append(str(i) +("[ ] "*6))


def show_board(board):
    for row in board:
        print((" ").join(row))

show_board(board)