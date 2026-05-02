from pieces.Piece import Piece


class Bishop(Piece):
    """Bishop is a subclass of the Piece class that holds the bishop movement logic"""

    def __init__(self, color):
        super().__init__(color, "Bi")

    def getMoves(self, board, pos):
        """TODO"""
        moves = []

        directions = [
            (-1, -1), # up left
            (-1, 1), # up right
            (1, -1), # down left
            (1, 1) # down right
        ]

        for direction in directions:
            moves.extend(self._walkDirection(board, pos, direction))

        return moves