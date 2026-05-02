from pieces.Piece import Piece


class Rook(Piece):
    """Rook is a subclass of the Piece class that holds the rook movement logic"""

    def __init__(self, color):
        super().__init__(color, "Ro")

    def getMoves(self, board, pos):

        moves = []

        directions = [
            (-1, 0), # up
            (1, 0), # down
            (0, -1), # left
            (0, 1) # right
        ]   

        for direction in directions:
            moves.extend(self._walkDirection(board, pos, direction))

        return moves



    