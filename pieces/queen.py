from pieces.Piece import Piece


class Queen(Piece):
    """Queen is a subclass of Piece that holds queen movement logic."""

    def __init__(self, color):
        super().__init__(color, "Qu")

    def getMoves(self, board, pos):
        """Return all legal queen moves from the current board position.

        The queen combines rook and bishop movement: it can move any number of
        squares along ranks, files, or diagonals until blocked by another piece.
        """
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]

        moves = []

        for direction in directions:
            moves.extend(self._walkDirection(board, pos, direction))

        return moves
