import random
import globals  # provided by the professor

# --- compatibility aliases (don't touch GAME/globals.py) ---
try:
    MINE = globals.MINE        # if prof used singular
except AttributeError:
    MINE = globals.MINES       # fallback if prof used plural


def place_random_mines(board, num_mines: int):
    rows, cols = len(board), len(board[0])
    assert 0 <= num_mines < rows * cols, "invalid number of mines"
    spots = [(r, c) for r in range(rows) for c in range(cols)]
    for r, c in random.sample(spots, k=num_mines):
        board[r][c] = MINE


# --- self-test only (safe to keep) ---
if __name__ == "__main__":
    import os, sys
    THIS_DIR = os.path.dirname(__file__)
    LAB_DIR = os.path.dirname(THIS_DIR)          # .../lab3
    GAME_DIR = os.path.join(LAB_DIR, "GAME")
    if GAME_DIR not in sys.path:
        sys.path.append(GAME_DIR)
    if THIS_DIR not in sys.path:
        sys.path.append(THIS_DIR)

    from initialize_board import initialize_board  # same folder import

    random.seed(42)  # reproducible
    b = initialize_board(3, 4, 0)
    place_random_mines(b, 3)
    for row in b:
        print(row)
    print("mine count:", sum(x == MINE for row in b for x in row))

