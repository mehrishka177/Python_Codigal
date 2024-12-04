pygame.init()
SCREEN_WIDTH, SCREEN_HIGHT = 500, 500

display_surface = pygame.dysplay.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption('Adding image and background image')

background_image = pygame.transform.scale(
    pygame.image.load('background.png').convert(),
    (SCREEN_WIDTH, SCREEN_HIGHT))

penguin_image = pygame.transform.scale(
    pygame.image.load('hello penguin.png').convert_alpha(), (200. 200))
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2,
                                              SCREEN_HIGHT // 2 - 30))

text = pygame.font.Font(None, 36).render('Hello World', True,
                                         pygame.Color('back'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HIGHT // 2 + 110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
                
        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_text)
        
        pygame.dysplay.flip()
        clock.tick(30)
        
    polygame.quit()
    
    
    
if __name__ == '__main__':
    game_loop()
        