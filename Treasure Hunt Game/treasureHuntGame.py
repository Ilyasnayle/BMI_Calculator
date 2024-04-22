import random

try:
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
except ValueError:
    print("Invalid input. Please enter integer values for rows and columns.")
    exit()

# Create the board
board = [['*' for _ in range(cols)] for _ in range(rows)]

try:
    treasure_row = int(input("Enter the row to hide the treasure (0 to {}): ".format(rows - 1)))
    treasure_col = int(input("Enter the column to hide the treasure (0 to {}): ".format(cols - 1)))
    if not (0 <= treasure_row < rows) or not (0 <= treasure_col < cols):
        print("Invalid location. Treasure must be placed within the board's dimensions.")
        exit()
except ValueError:
    print("Invalid input. Please enter integer values for row and column.")
    exit()

# Place the treasure
board[treasure_row][treasure_col] = 'T'

# Place the trap
trap_row, trap_col = random.randint(0, rows - 1), random.randint(0, cols - 1)
while (trap_row, trap_col) == (treasure_row, treasure_col):
    trap_row, trap_col = random.randint(0, rows - 1), random.randint(0, cols - 1)
board[trap_row][trap_col] = 'X'

# Print the board
print("\nHere is the board:")
for row in board:
    print(' '.join(row))

# Game loop
while True:
    try:
        guess_row = int(input("\nEnter your guess for the row (0 to {}): ".format(rows - 1)))
        guess_col = int(input("Enter your guess for the column (0 to {}): ".format(cols - 1)))
        if not (0 <= guess_row < rows) or not (0 <= guess_col < cols):
            print("Invalid location. Guess must be within the board's dimensions.")
            continue
    except ValueError:
        print("Invalid input. Please enter integer values for row and column.")
        continue

    # Check the guess
    if board[guess_row][guess_col] == 'T':
        print("\nCongratulations! You found the treasure!")
        break
    elif board[guess_row][guess_col] == 'X':
        print("\nOops! You've been trapped by a trap!")
        break
    else:
        print("\nSorry, not this time. Try again!")
