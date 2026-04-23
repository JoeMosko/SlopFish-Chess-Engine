import Board
from PygameBoard import py_game_board
def main():
    board = Board.Board(empty=False)
    board.toString()
    py_game_board()


if __name__ == "__main__":
    main()