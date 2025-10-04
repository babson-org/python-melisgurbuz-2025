def ai_move(board: list[int]):
    """
        Simple AI that selects the first available cell.
        Remember board is a list that starts with items 1 - 9
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        after two moves with X choosing 1 and O choosing 5 the board looks like:
        [10, 2, 3, 4, -10, 6, 7, 8, 9]
        
        so in this case your function should return 2
    """
    # TODO: Loop through board

    # TODO: Find the first index where abs(cell) != 10


    # TODO: Return that index as the AI's move
def ai_move(board: list[int]) -> int:
    """
    Simple AI: select the first available cell.
    Returns the 0-based index to play.
    """
    for i in range(len(board)):
        cell = board[i]
        if abs(cell) != 10:          # open if not X(10) or O(-10)
            return i                 # first open index
    raise ValueError("No available moves.")
