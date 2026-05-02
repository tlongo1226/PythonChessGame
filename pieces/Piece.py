
class Piece:
    def __init__(self, color, label):
        self.color = color
        self.alive = True
        self.label = label

    """
        getMoves returns the available moves to a Piece based on the piece label
    """
        # -------------------- ENTRY POINT --------------------


    def getMoves(self, board, pos):
        """getMoves is a function implemented in each Piece subclass """
        raise NotImplementedError("Subclasses must implement getMoves")
    

    def setFirstTurn(self, isFirstTurn):
        raise NotImplementedError("Subclasses must implement getMoves")

    def _walkDirection(self, board, start, direction):
        """walkDirection is a helper class that allows easier movement for pieces that can move multiple squares at a time"""
        moves = []
        row, col = start
        dRow, dCol = direction

        currRow = row + dRow
        currCol = col + dCol

        while board.isOnBoard((currRow, currCol)):
            pos = (currRow, currCol)
             
            if board.isEmpty(pos):
                moves.append(pos)

            elif board.isEnemy(pos, self.color):
                moves.append(pos)
                break
            else:
                break # friendly piece blocks

            currRow += dRow
            currCol += dCol
            

        return moves
    
    def capture(self):
        """capture is a helper funct to allow capture of pieces. Used to show the pieces in a "graveyard" of captured pieces"""
        self.alive = False