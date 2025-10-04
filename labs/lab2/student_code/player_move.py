    
def player_move(board: list[int], score: dict[str, int]):
    """
        Prompts the player to choose a valid move.
        Remember score is a dictionary from play_game()
        It has two keys 'player' and 'ai' associated values
        are 10 and -10 depending on who goes first.
    """
    """
    Prompts the player to choose a valid move and writes it to the board.
    """
    prompt = "Select an empty cell (1-9): "
    while True:
        try:
            # TODO: Convert input to integer
            move = int(input(prompt).strip())

            # TODO: Validate move is in range and not taken
            if move < 1 or move > 9:
                raise ValueError  

            idx = move - 1  # map 1..9 -> 0..8
            if abs(board[idx]) == 10:  # taken by X(10) or O(-10)
                prompt = "That cell is taken. Choose another (1-9): "
                continue

            break  # valid choice -> exit loop

        except ValueError:
            prompt = "Invalid input. Try again (1-9): "

    # TODO: Assign score['player'] to the selected cell on the board
    # HINT: board moves are 1..9 but indices are 0..8
    board[idx] = score['player']
