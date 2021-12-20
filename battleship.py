from random import randint

board = []
player = "choice"
play = "y"

while play == "y":
    
    i = 2

    while(i < 3 or i > 9):
        i = int(input("Enter the size of the board (3-9): "))
        if i < 3:
            print("Choose a size larger than 2!")
        elif i > 9:
            print("Choose a size smaller than 10!")
    
    for x in range(i):
        board.append(["O"] * i)
    
    def print_board(board):
        for row in board:
            print((" ").join(row))

    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(0, len(board[0]) - 1)

    print(" ========== Battleship ========== ")
    print_board(board)

    ship_row = random_row(board)
    ship_col = random_col(board)

for round in range(9):
    print("Round", round)
    guess_row = int(input("Guess the row: "))
    guess_col = int(input("Guess the column: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 5):
            print("LOL, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            board[guess_row][guess_col] = "X"
    
    if round == 8:
        print("Game Over!")
    round += 1
    print_board(board)