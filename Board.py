from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.king import King
from pieces.queen import Queen
from pieces.pawn import Pawn
from pieces.knight import Knight


class Board:
    def __init__(self):
        self.grid = {}
        self.setup()

    def setup(self):
        """setupgrid add the pieces on the grid to the grid dict"""
        # Pawns
        for col in range(8):
            self.grid[(6, col)] = Pawn("white")
            self.grid[(1, col)] = Pawn("black")

        # Rooks
        for col in [0, 7]:
            self.grid[(7, col)] = Rook("white")
            self.grid[(0, col)] = Rook("black")

        # Knights
        for col in [1, 6]:
            self.grid[(7, col)] = Knight("white")
            self.grid[(0, col)] = Knight("black")

        # Bishops
        for col in [2, 5]:
            self.grid[(7, col)] = Bishop("white")
            self.grid[(0, col)] = Bishop("black")

        # Queens
        self.grid[(7, 3)] = Queen("white")
        self.grid[(0, 3)] = Queen("black")

        # Kings
        self.grid[(7, 4)] = King("white")
        self.grid[(0, 4)] = King("black")

        print("GRID: ")

    def getPiece(self, pos):
        """getPiece returns the piece from"""
        return self.grid.get(pos)

    # -------------------- MOVEMENT --------------------
    def movePiece(self, start, end):
        """TODO"""
        piece = self.grid[start]
        if piece.label == "Pa":
            if piece.isPromotion(end):
                print("Promotion identified")
                self.grid[end] = piece
                del self.grid[start]
                return (end, piece.color)
            # uses the setFirstTurn within the pawn class to signal to the pawn inst that it succesfully took it's first turn
            if piece.firstTurn:
                piece.setFirstTurn(False)
        self.grid[end] = piece
        del self.grid[start]
        return None

    def promotePiece(self, promotionTup, promoType):
        """promotePiece will place a promoted pawn on the end location provided. It will use the row col selected on the PromotionWindow to determine the type."""
        # Queen
        if promoType == (0, 0):
            self.grid[promotionTup[0]] = Queen(promotionTup[1])

        # Rook
        elif promoType == (0, 1):
            self.grid[promotionTup[0]] = Rook(promotionTup[1])

        # Bishop
        elif promoType == (1, 0):
            self.grid[promotionTup[0]] = Bishop(promotionTup[1])
        # Kn
        elif promoType == (1, 1):
            self.grid[promotionTup[0]] = Knight(promotionTup[1])
        else:
            print(
                "Bad type idk how this happened, somehow a promotion type not expected was passed in:",
                promoType,
            )

    # -------------------- GETTERS --------------------
    def getPiece(self, pos):
        """getPiece takes in a (row, col) and grabs the Piece stored in that key within the grid dictionary. This will return the Piece object it finds or produce a Key Error"""
        return self.grid.get(pos)

    def hasPiece(self, pos):
        """hasPiece determines if the passed in (row, col) inside pos is a valid key for the grid dict"""
        return pos in self.grid

    # -------------------- HELPERS --------------------
    def isOnBoard(self, pos):
        """TODO"""
        row, col = pos
        return 0 <= row < 8 and 0 <= col < 8

    def isEmpty(self, pos):
        """TODO"""
        return pos not in self.grid

    def isEnemy(self, pos, color):
        """TODO"""
        return pos in self.grid and self.grid[pos].color != color

    def isFriendly(self, pos, color):
        """TODO"""
        return pos in self.grid and self.grid[pos].color == color
