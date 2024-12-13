from board import Board

def minimax(board, depth, is_maximizing):
    winner = board.check_winner()
    if winner != 0:  # Someone has won
        return winner
    if board.is_full():  # It's a draw
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in board.get_available_moves():
            board.make_move(move, 1)  # AI plays as 'X'
            score = minimax(board, depth + 1, False)
            board.make_move(move, 0)  # Undo the move
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in board.get_available_moves():
            board.make_move(move, -1)  # Opponent plays as 'O'
            score = minimax(board, depth + 1, True)
            board.make_move(move, 0)  # Undo the move
            best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -float('inf')
    best_move = None
    for move in board.get_available_moves():
        board.make_move(move, 1)  # AI plays as 'X'
        score = minimax(board, 0, False)
        board.make_move(move, 0)  # Undo the move
        if score > best_score:
            best_score = score
            best_move = move
    return best_move
