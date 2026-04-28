class Piece:
    def __init__(self, type: str, value: int, team: bool, img: str ):
        self.type = type
        self.value = value
        self.team = team
        self.img = img
    #calculate if new square is a legal knight move 
    #TODO: check if current pin 
    def get_legal_move(self, new_square) -> bool:
        match(self.type):
            case "knight":
                return
                #return get_knight_move(new_square)
            case "pawn":
                return 
            case "bishop":
                return
            case "king":
                return