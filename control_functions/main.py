from time import sleep
from datetime import datetime
import pygame
import sys
import functions
import helpers


pygame.init()


größe = (800, 600)
bildschirm = pygame.display.set_mode(größe)

font = pygame.font.Font('/home/levi/Downloads/DIGITALDREAMNARROW.ttf', 36)

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 
    
    zeit = datetime.now()
    aktuelle_zeit = zeit.strftime("%H:%M")
    
    stunde_str = zeit.strftime("%H")
    stunde = int(stunde_str)
    
    minute_str = zeit.strftime("%M")
    minute = int(minute_str)



    schrift_stunde = font.render(str(helpers.aufgabe_für_stunde(stunde)), True, (255, 255, 255))
    ausgabe_stunde = schrift_stunde.get_rect(center=(400, 300))

    schrift_minute = font.render(str(helpers.aufgabe_für_minute(minute)), True, (255, 255, 255))
    ausgabe_minute = schrift_minute.get_rect(center=(400, 700))

    bildschirm.fill((0, 0, 0)) 
    bildschirm.blit(schrift_stunde, ausgabe_stunde)
    bildschirm.blit(schrift_minute, ausgabe_minute)

    pygame.display.flip()
    sleep(5)

pygame.quit()
sys.exit()
