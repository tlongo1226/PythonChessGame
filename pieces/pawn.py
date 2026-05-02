from pieces.Piece import Piece

class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color, "Pa")
        self.firstTurn = True # used to track if it is the first move of the pawn
    
    def getMoves(self, board, pos):
        """getMoves will provide a list containing the (row, col) of each possible move for the pawn. It will use the firstTurn bool to determine if it is the first turn and the pawn can move two spaces instead of one. """
        moves = []
        row, col = pos

        # direction depends on color
        direction = -1 if self.color == "white" else 1
        
        forward = (row + direction, col)
        diagonals = [
            (row + direction, col - 1),
            (row + direction, col + 1)
        ]
        
        # forward move (must be empty)
        if board.isOnBoard(forward) and board.isEmpty(forward):
            moves.append(forward)

        #Moves two on first turn
        if self.firstTurn:
            twoStep = -2 if self.color == "white" else 2
            forward = (row + twoStep, col)
            if board.isOnBoard(forward) and board.isEmpty(forward):
                moves.append(forward)


        # capture moves (must be enemy)
        for diag in diagonals:
            if board.isOnBoard(diag) and board.isEnemy(diag, self.color):
                moves.append(diag)

        return moves
    
    def isPromotion(self, pos):
        """TODO"""
        row, col = pos
        if self.color == "white" and row == 0:
            return True
        elif self.color == "black" and row == 7:
            return True
        return False
    
    def setFirstTurn(self, isFirstTurn):
        """setFirstTurn allows the user to pass in a bool to set the firstTurn variable to"""
        self.firstTurn = isFirstTurn
    