from pieces.Piece import Piece


class King(Piece):
    """King is a subclass of the Piece class that holds King movement logic"""

    def __init__(self, color):
        super().__init__(color, "Ki")

    def getMoves(self, board, pos):
        moves = []
        row, col = pos
        directions = [ 
            (row + 1, col), # dowm
            (row - 1, col), # up
            (row, col - 1), # left
            (row, col + 1), # right
            (row + 1, col + 1), # down right
            (row + 1, col - 1), # down left
            (row - 1, col + 1), # up right
            (row - 1, col - 1), # up left
        ]
        for direction in directions:
            if (board.isOnBoard(direction) and board.isEmpty(direction)) or board.isEnemy(direction, self.color):
                moves.append(direction)

        return moves