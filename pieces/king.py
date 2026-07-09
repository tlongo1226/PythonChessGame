from pieces.Piece import Piece


class King(Piece):
    """King is a subclass of Piece that holds king movement logic."""

    def __init__(self, color):
        super().__init__(color, "Ki")

    def getMoves(self, board, pos):
        """Return all legal king moves from the current board position.

        The king can move one square in any direction, including diagonals.
        It may move to any empty square or capture an enemy piece, but it cannot
        move onto a square occupied by a friendly piece.
        """
        moves = []
        row, col = pos
        directions = [
            (row + 1, col),  # down
            (row - 1, col),  # up
            (row, col - 1),  # left
            (row, col + 1),  # right
            (row + 1, col + 1),  # down-right
            (row + 1, col - 1),  # down-left
            (row - 1, col + 1),  # up-right
            (row - 1, col - 1),  # up-left
        ]

        for direction in directions:
            if (
                board.isOnBoard(direction) and board.isEmpty(direction)
            ) or board.isEnemy(direction, self.color):
                moves.append(direction)

        return moves
