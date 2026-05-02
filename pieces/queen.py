from pieces.Piece import Piece


class Queen(Piece):
    """Queen is a subclass of the Piece class that hold the logic of queen movement"""

    def __init__(self, color):
        super().__init__(color, "Qu")

    def getMoves(self, board, pos):
        """TODO"""
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]

        moves = []

        for direction in directions:
            moves.extend(self._walkDirection(board, pos, direction))

        return moves
