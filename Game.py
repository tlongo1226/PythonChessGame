from Board import Board
import random


class Game:
    """Game contains the rules and state of the chess board."""

    def __init__(self):
        self.board = Board()
        self.selectedSquare = None
        self.currentTurn = random.choice(["white", "black"])
        self.turnCounter = 1
        self.pendingPromotion = None
        print("First turn:", self.currentTurn)

    def handleClicks(self, clickedPos):
        """handleClicks determines what should be done based on where the user clicks. It uses multiple helper functions within the UI.py class to determine where in the window the user clicked."""

        if self.pendingPromotion:
            self.board.promotePiece(self.pendingPromotion, clickedPos)
            self.pendingPromotion = None
            return

        piece = self.board.getPiece(clickedPos)
        # --- Nothing selected yet ---
        if self.selectedSquare is None:
            if piece and piece.color == self.currentTurn:
                self.selectedSquare = clickedPos
                print("Selected:", clickedPos)
            return

        # --- Something already selected ---
        moves = self.getValidMoves()

        # deselect
        if clickedPos == self.selectedSquare:
            self.selectedSquare = None
            return

        # valid move (includes capture)
        if clickedPos in moves:
            result = self.board.movePiece(self.selectedSquare, clickedPos)

            if result:
                pos, color = result
                self.pendingPromotion = (pos, color)
            print("Moved:", self.selectedSquare, "->", clickedPos)
            self.currentTurn = "black" if self.currentTurn == "white" else "white"
            self.turnCounter += 1
            self.selectedSquare = None
            return

        # switch selection (friendly piece)
        if piece and piece.color == self.currentTurn:
            self.selectedSquare = clickedPos
            print("Switched selection:", clickedPos)
            return

        # invalid move
        print("Invalid move:", self.selectedSquare, "->", clickedPos)
        self.selectedSquare = None

    def getValidMoves(self):
        """getValidMoves determines the available moves based on the passed piece"""
        if self.selectedSquare is None:
            return []

        piece = self.board.getPiece(self.selectedSquare)
        if not piece:
            return []
        moves = piece.getMoves(self.board, self.selectedSquare)

        # lambda prevent empty moves from being returned
        return moves if moves is not None else []
