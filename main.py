import pygame
import sys

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 720
BUTTON_WIDTH, BUTTON_HEIGHT = 120, 60
WHITE = (255, 255, 255)
BG_COLOR = (50, 153, 50)
BUTTON_COLOR = (255, 102, 0)
BUTTON_HOVER_COLOR = (255, 153, 51)
BUTTON_TEXT_COLOR = (255, 255, 255)

# Main window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Rat race project")

font = pygame.font.Font(None, 30)
button_text = ["Race", "Train", "Exit"]

buttons = []
for i in range(3):
    button = pygame.Rect(
        WINDOW_WIDTH // 2 - BUTTON_WIDTH // 2,
        200 + i * 100,
        BUTTON_WIDTH,
        BUTTON_HEIGHT,
    )
    buttons.append(button)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, button in enumerate(buttons):
                    if button.collidepoint(event.pos):
                        if i == 0:
                            print("Race button clicked")
                        elif i == 1:
                            print("Train button clicked")
                        elif i == 2:
                            pygame.quit()
                            sys.exit()

    window.fill(BG_COLOR)

    for i, button in enumerate(buttons):
        pygame.draw.rect(
            window,
            BUTTON_COLOR if button.collidepoint(pygame.mouse.get_pos()) else BUTTON_HOVER_COLOR,
            button,
        )
        text = font.render(button_text[i], True, BUTTON_TEXT_COLOR)
        text_rect = text.get_rect(center=button.center)
        window.blit(text, text_rect)

    pygame.display.flip()
