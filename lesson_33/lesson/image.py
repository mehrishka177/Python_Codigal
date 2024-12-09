import pygame
import os

pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

# Set up display
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')

# Load and scale background image
if not os.path.exists('background.png'):
    print("Error: 'background.png' not found!")
    pygame.quit()
    exit()
background_image = pygame.transform.scale(
    pygame.image.load('background.png').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# Load and scale penguin image
if not os.path.exists('hello_penguin.png'):
    print("Error: 'hello_penguin.png' not found!")
    pygame.quit()
    exit()
penguin_image = pygame.transform.scale(
    pygame.image.load('hello_penguin.png').convert_alpha(),
    (200, 200)
)
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))

# Render text
text = pygame.font.Font(None, 36).render('Hello World', True, pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

# Game loop
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw everything
        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)

        # Update display
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()
