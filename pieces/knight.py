from pieces.Piece import Piece

class Knight(Piece):
    """Knight is subclass of the Piece class that contains the movement logic for Knight pieces"""

    def __init__(self, color):
        super().__init__(color, "Kn")

    def getMoves(self, board, pos):
        moves = []

        row, col = pos

        offsets = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            ( 1, -2), ( 1, 2),
            ( 2, -1), ( 2, 1)
        ]

        for dRow, dCol in offsets:
            newPos = (row + dRow, col + dCol)

            if not board.isOnBoard(newPos):
                continue

            if board.isEmpty(newPos) or board.isEnemy(newPos, self.color):
                moves.append(newPos)

        return moves