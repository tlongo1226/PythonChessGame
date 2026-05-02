from pieces.Piece import Piece

class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color, "Pa")
        self.firstTurn = True # used to track if it is the first move of the pawn
    
    def getMoves(self, board, pos):
        """Return all legal pawn moves from the current board position.

        Pawns move one square forward into an empty square. On their first move,
        pawns may move two squares forward when both the intermediate and target
        squares are empty. Pawns may capture diagonally one square forward if an
        enemy piece occupies that square.
        """
        moves = []
        row, col = pos

        # Direction depends on color: white moves up the board, black moves down.
        direction = -1 if self.color == "white" else 1

        oneStep = (row + direction, col)
        twoStep = (row + 2 * direction, col)
        diagonals = [
            (row + direction, col - 1),
            (row + direction, col + 1)
        ]

        # One-square forward move must be empty.
        if board.isOnBoard(oneStep) and board.isEmpty(oneStep):
            moves.append(oneStep)

            # Two-square first move is only allowed if the pawn has not moved yet and
            # the destination square is empty.
            if self.firstTurn and board.isOnBoard(twoStep) and board.isEmpty(twoStep):
                moves.append(twoStep)

        # Capture moves: diagonally forward onto an enemy piece.
        for diag in diagonals:
            if board.isOnBoard(diag) and board.isEnemy(diag, self.color):
                moves.append(diag)

        return moves
    
    def isPromotion(self, pos):
        """Return True when the pawn reaches the promotion rank."""
        row, col = pos
        if self.color == "white" and row == 0:
            return True
        elif self.color == "black" and row == 7:
            return True
        return False
    
    def setFirstTurn(self, isFirstTurn):
        """Update the pawn's first-turn flag after its initial move."""
        self.firstTurn = isFirstTurn
    