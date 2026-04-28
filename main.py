import LogicBoard
from PygameBoard import pygame_board
def main():
    board = LogicBoard.LogicBoard(empty=False)
    board.toString()
    pygame_board()


if __name__ == "__main__":
    main()