from pieces.Piece import Piece

class Knight(Piece):
    """Knight is a subclass of Piece that contains knight movement logic."""

    def __init__(self, color):
        super().__init__(color, "Kn")

    def getMoves(self, board, pos):
        """Return all legal knight moves from the current board position.

        The knight moves in an L-shape: two squares in one direction and one
        square perpendicular to that direction. It can jump over other pieces,
        and may move to an empty square or capture an enemy piece.
        """
        moves = []

        row, col = pos

        offsets = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2),  (1, 2),
            (2, -1),  (2, 1)
        ]

        for dRow, dCol in offsets:
            newPos = (row + dRow, col + dCol)

            if not board.isOnBoard(newPos):
                continue

            if board.isEmpty(newPos) or board.isEnemy(newPos, self.color):
                moves.append(newPos)

        return moves