from pieces.Piece import Piece


class Rook(Piece):
    """Rook is a subclass of Piece that holds rook movement logic."""

    def __init__(self, color):
        super().__init__(color, "Ro")

    def getMoves(self, board, pos):
        """Return all legal rook moves from the current board position.

        The rook moves any number of squares vertically or horizontally until it
        encounters another piece. It may capture an enemy piece on the first
        occupied square it reaches in any direction.
        """
        moves = []

        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1)    # right
        ]

        for direction in directions:
            moves.extend(self._walkDirection(board, pos, direction))

        return moves



    