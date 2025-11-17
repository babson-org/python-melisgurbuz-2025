def initialize_board(rows, cols, fill_value):
    """
    Create an empty board with the given dimensions and fill value.
    """
    return [[fill_value for _ in range(cols)] for _ in range(rows)]

