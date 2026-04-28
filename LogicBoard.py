class LogicBoard:
    #declare points for each piece
    PAWN = 1
    KNIGHT = BISHOP = 3
    ROOK = 5
    QUEEN = 9
    KING = 10
    
    def __init__(self, empty: bool):
        #initialize empty 8x8 board
        if empty:
            self.board = [[0 for x in range(8)] for y in range(8)]
        #initialize with pieces 
        else:
            self.board = [[5, 3, 3, 9, 10, 3, 3, 5],
                          [1, 1, 1, 1, 1, 1, 1, 1,],
                          [0, 0, 0, 0, 0, 0, 0, 0,],
                          [0, 0, 0, 0, 0, 0, 0, 0,],
                          [0, 0, 0, 0, 0, 0, 0, 0,],
                          [0, 0, 0, 0, 0, 0, 0, 0,],
                          [1, 1, 1, 1, 1, 1, 1, 1,],
                          [5, 3, 3, 9, 10, 3, 3, 5],
                          ]
    def toString(self):
        result = ""
        for i in range(8):
            for j in range(8):
                result += str(self.board[i][j])
            result += "\n"
        print(result)
        return


