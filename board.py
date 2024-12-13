import numpy as np

class Board:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)

    def print_board(self):
        symbols = {0: ".", 1: "X", -1: "O"}
        for row in self.board:
            print(" ".join(symbols[cell] for cell in row))
        print()

    def check_winner(self):
        for player in [1, -1]:  # Check for both players
            # Check rows, columns, and diagonals
            if any(np.sum(row) == 3 * player for row in self.board) or \
               any(np.sum(col) == 3 * player for col in self.board.T) or \
               np.trace(self.board) == 3 * player or \
               np.trace(np.fliplr(self.board)) == 3 * player:
                return player
        return 0  # No winner yet

    def is_full(self):
        return not (self.board == 0).any()

    def get_available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == 0]

    def make_move(self, move, player):
        self.board[move] = player
