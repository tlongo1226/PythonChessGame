import pygame
import colors


class UI:
    def __init__(self, screen):
        # -------------------- Member Vars --------------------------------
        self.WIDTH, self.HEIGHT = 800, 800
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.boardStart = 150
        self.squareLength = 62
        self.boardSize = self.squareLength * 8
        self.font = pygame.font.Font(None, int(self.squareLength * 0.5))

        self.promoSize = 80
        self.promoStart = 300
        self.promoOptions = ["Qu", "Ro", "Bi", "Kn"]
        pygame.display.set_caption("Chess")

    # -------------------- Class functions ----------------------------
    def draw(self, board, selectedSquare, moves, currentTurn):
        """TODO"""
        self.drawSquares()
        self.drawPieces(board)
        self.drawHighlight(selectedSquare)
        self.drawValidMoves(moves)
        self.drawTurnIndicator(currentTurn)

    def drawValidMoves(self, moves):
        """TODO"""
        if not moves:
            return
        for row, col in moves:
            x = self.boardStart + col * self.squareLength
            y = self.boardStart + row * self.squareLength

            pygame.draw.rect(
                self.screen,
                colors.POSSIBLE_MOVE,
                (x, y, self.squareLength, self.squareLength),
                3,
            )

    def drawSquares(self):
        """drawSquares draws the board itself"""
        for col in range(8):
            for row in range(8):
                x = self.boardStart + col * self.squareLength
                y = self.boardStart + row * self.squareLength

                if (row + col) % 2 == 0:
                    color = colors.WHITE_SQUARE
                else:
                    color = colors.BLACK_SQUARE

                pygame.draw.rect(
                    self.screen, color, (x, y, self.squareLength, self.squareLength)
                )

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------ Draw Components--------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    def drawPieces(self, board):
        """drawPieces draws the pieces"""
        for (row, col), piece in board.grid.items():
            x = self.boardStart + col * self.squareLength
            y = self.boardStart + row * self.squareLength

            centerX = x + self.squareLength // 2
            centerY = y + self.squareLength // 2

            color = colors.WHITE_PIECE if piece.color == "white" else colors.BLACK_PIECE

            pygame.draw.circle(
                self.screen, color, (centerX, centerY), int(self.squareLength * 0.4)
            )

            text = self.font.render(
                piece.label,
                True,
                (0, 0, 0) if piece.color == "white" else (255, 255, 255),
            )
            text_rect = text.get_rect(center=(centerX, centerY))
            self.screen.blit(text, text_rect)

    def drawTurnIndicator(self, currentTurn):
        """drawTurnIndicator creates a circle with text that indicates the color"""
        badge_color = (
            colors.WHITE_PIECE if currentTurn == "white" else colors.BLACK_PIECE
        )
        text = self.font.render(
            f"Turn: {currentTurn.capitalize()}", True, colors.TURN_TEXT
        )

        padding_x = 12
        padding_y = 8
        box_width = text.get_width() + padding_x * 2
        box_height = text.get_height() + padding_y * 2
        box_rect = pygame.Rect(20, 20, box_width, box_height)

        pygame.draw.rect(self.screen, badge_color, box_rect)
        self.screen.blit(text, (box_rect.x + padding_x, box_rect.y + padding_y))

    def drawHighlight(self, selectedSquare):
        """drawHighlight will draw a highlight around the selected square"""
        if selectedSquare is None:
            return
        row, col = selectedSquare
        x = self.boardStart + col * self.squareLength
        y = self.boardStart + row * self.squareLength
        pygame.draw.rect(
            self.screen,
            colors.SELECTED_HIGHLIGHT,
            (x, y, self.squareLength, self.squareLength),
            3,
        )

    def isInsideBoard(self, mouseX, mouseY):
        """isInsideBoard will determine if the user click was inside the board"""
        return (
            self.boardStart <= mouseX < self.boardStart + self.boardSize
            and self.boardStart <= mouseY < self.boardStart + self.boardSize
        )

    def getSquareFromMouse(self, mouseX, mouseY):
        """getSquareFromMouse is a helper function to determine if the user click was inside the board square"""
        col = (mouseX - self.boardStart) // self.squareLength
        row = (mouseY - self.boardStart) // self.squareLength
        return int(row), int(col)

    def isInsidePromotion(self, mouseX, mouseY):
        """isInsidePromotion determines if the user click was inside the promotion "popup". This requires multiplying the promoSize by two due to the fact from size is actually only the size of a single square in the promotion window"""
        return (
            self.promoStart <= mouseX < self.promoStart + self.promoSize * 2
            and self.promoStart <= mouseY < self.promoStart + self.promoSize * 2
        )
        pass

    def getPromotionSquare(self, mouseX, mouseY):
        """TODO"""
        col = (mouseX - self.promoStart) // self.promoSize
        row = (mouseY - self.promoStart) // self.promoSize
        return int(row), int(col)

    def drawPromotion(self, color):
        """drawPromotion will take in the potential promotion color and display a promotion window in the center of the screen. The window will allow the user to select an option to promote a pawn."""
        outerRect = pygame.Rect(
            self.promoStart - 50,
            self.promoStart - 50,
            self.promoSize + 180,
            self.promoSize + 180,
        )
        tileColor = colors.WHITE_PIECE if color == "white" else colors.BLACK_PIECE
        otherColor = colors.BLACK_PIECE if color == "white" else colors.WHITE_PIECE
        pygame.draw.rect(self.screen, colors.TURN_TEXT, outerRect)
        for i, label in enumerate(self.promoOptions):
            row = i // 2
            col = i % 2

            x = self.promoStart + col * self.promoSize
            y = self.promoStart + row * self.promoSize

            rect = pygame.Rect(x, y, self.promoSize, self.promoSize)
            pygame.draw.rect(self.screen, otherColor, rect)

            center = (x + self.promoSize // 2, y + self.promoSize // 2)

            pygame.draw.circle(self.screen, tileColor, center, 25)

            text = self.font.render(label, True, otherColor)
            textRect = text.get_rect(center=center)
            self.screen.blit(text, textRect)

        separator_x = self.promoStart + self.promoSize
        separator_y = self.promoStart + self.promoSize
        pygame.draw.line(
            self.screen,
            tileColor,
            (separator_x, self.promoStart),
            (separator_x, self.promoStart + 2 * self.promoSize),
            2,
        )
        pygame.draw.line(
            self.screen,
            tileColor,
            (self.promoStart, separator_y),
            (self.promoStart + 2 * self.promoSize, separator_y),
            2,
        )
