from board import Board
from ai import find_best_move

def play_game():
    board = Board()
    print("Welcome to Tic Tac Toe!")
    print("You are 'O'. AI is 'X'.")
    board.print_board()

    while True:
        # Player's turn
        print("Your turn!")
        move = None
        while move not in board.get_available_moves():
            try:
                row, col = map(int, input("Enter your move (row and column, 0-indexed): ").split())
                move = (row, col)
            except ValueError:
                print("Invalid input. Try again.")
        
        board.make_move(move, -1)  # Player plays as 'O'
        board.print_board()

        # Check if player won
        if board.check_winner() == -1:
            print("Congratulations! You won!")
            break
        if board.is_full():
            print("It's a draw!")
            break

        # AI's turn
        print("AI's turn...")
        ai_move = find_best_move(board)
        board.make_move(ai_move, 1)  # AI plays as 'X'
        board.print_board()

        # Check if AI won
        if board.check_winner() == 1:
            print("AI wins! Better luck next time.")
            break
        if board.is_full():
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
