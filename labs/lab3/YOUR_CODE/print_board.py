import globals

def print_board(board: list, level: int):

    board = [
        [(' ♦', '💣'), (' ♦', '💣'), (' ♦', 1),
         (' ♦', '   '), (' ♦', '   '), (' ♦', '   ')],
        [(' ♦', 2), (' ♦', 2), (' ♦', 1),
         (' ♦', '   '), (' ♦', '   '), (' ♦', '   ')],
        [(' ♦', '   '), (' ♦', '   '), (' ♦', '   '),
         (' ♦', '   '), (' ♦', '   '), (' ♦', '   ')],
    ]

    level = 0

    line_hash = '|-----'

     # Printing the header row with column indexes
    print('      ', end='')
    for idx in range(globals.COLS):
        print(f'   {idx}  ', end='')

    print(f'\n      {line_hash * globals.COLS}|')

    # Printing each row of the board
    for row in range(globals.ROWS):
        print(f'  {row}   ', end='')  # Row indicator

        for col in range(globals.COLS):
            symbol = board[row][col][level]  # Get the correct level of the tuple

            if symbol == '💣':  # If it is a bomb, print with a special format
                print(f'| {symbol:3}', end='')
            else:
                print(f'| {symbol:3} ', end='')  # Print the symbol

        print('|')  # End of the row

        # Printing the line separator after each row
        print(f'      {line_hash * globals.COLS}|')

# Sample call to print_board with 4 as the level index (you can adjust the level based on your game logic)
print_board(board, 0)