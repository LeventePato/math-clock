from time import sleep
from datetime import datetime
import pygame
import sys #???

# Initialize Pygame
pygame.init()

# Set up the display
#size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
size = (800, 600)
screen = pygame.display.set_mode(size)

# Set up the font
font = pygame.font.Font('/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf', 72)
# Main loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 
    
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    stunde = now.strftime("%H")
    minute = now.strftime("%M")
    
    # Render the text
    text = font.render(str(current_time), True, (255, 255, 255))  # White text
    text_rect = text.get_rect(center=(size[0] / 2, size[1] / 2))

    # Clear the screen and set the screen background
    screen.fill((0, 0, 0))  # Black background
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()
    sleep()

# Quit Pygame
pygame.quit()
sys.exit()


