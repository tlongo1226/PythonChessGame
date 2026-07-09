import pygame
import sys
import colors
from Game import Game
from ui import UI

# -------------------- Member Vars ----------------------------

# -------------------- Class functions ----------------------------

# -------------------- INIT ----------------------------
pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

clock = pygame.time.Clock()

# Create core objects
game = Game()
ui = UI(screen=screen)

running = True

while running:
    # -------- INPUT --------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos

            if ui.isInsideBoard(mouseX, mouseY) and game.pendingPromotion == None:
                square = ui.getSquareFromMouse(mouseX, mouseY)
                game.handleClicks(square)

            if game.pendingPromotion and ui.isInsidePromotion(mouseX, mouseY):
                promo = ui.getPromotionSquare(mouseX, mouseY)
                print("WOOHOO MADE IT INSIDE PROMOTION with promo:", promo)
                game.handleClicks(promo)

    # -------- DRAW --------
    screen.fill(colors.MAIN_BACKGROUND)

    moves = game.getValidMoves()
    ui.draw(game.board, game.selectedSquare, moves, game.currentTurn)
    if game.pendingPromotion:
        ui.drawPromotion(game.pendingPromotion[1])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
