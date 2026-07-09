from pieces.Piece import Piece


class Bishop(Piece):
    """Bishop is a subclass of Piece that holds bishop movement logic."""

    def __init__(self, color):
        super().__init__(color, "Bi")

    def getMoves(self, board, pos):
        """Return all legal bishop moves from the current board position.

        The bishop moves diagonally in any direction until it hits the edge
        of the board, a friendly piece, or an enemy piece that it can capture.
        """
        moves = []

        directions = [
            (-1, -1),  # up-left diagonal
            (-1, 1),  # up-right diagonal
            (1, -1),  # down-left diagonal
            (1, 1),  # down-right diagonal
        ]

        for direction in directions:
            moves.extend(self._walkDirection(board, pos, direction))

        return moves
