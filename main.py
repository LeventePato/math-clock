from time import sleep
from datetime import datetime
import pygame
import sys
import functions
import helpers


pygame.init()


größe = (480, 320)
bildschirm = pygame.display.set_mode(größe, pygame.FULLSCREEN)

pygame.mouse.set_visible(False)

font = pygame.font.Font('./font/DIGITALDREAMNARROW.ttf', 48)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 
    
    zeit = datetime.now()

    stunde_str = zeit.strftime("%H")
    stunde = int(stunde_str)
    
    minute_str = zeit.strftime("%M")
    minute = int(minute_str)


    aufgabe_für_stunde_str = helpers.aufgabe_für_stunde_berechnen(stunde)
    aufgabe_für_stunde =  "%.2d%s%.2d%s%.2d h" % (aufgabe_für_stunde_str[0], aufgabe_für_stunde_str[1], aufgabe_für_stunde_str[2], aufgabe_für_stunde_str[3], aufgabe_für_stunde_str[4])

    aufgabe_für_minute_str = helpers.aufgabe_für_minute_berechnen(minute)
    aufgabe_für_minute = "%.2d%s%.2d%s%.2d m" % (aufgabe_für_minute_str[0], aufgabe_für_minute_str[1], aufgabe_für_minute_str[2], aufgabe_für_minute_str[3], aufgabe_für_minute_str[4])


    schrift_stunde = font.render(aufgabe_für_stunde, True, (255, 255, 255))
    ausgabe_stunde = schrift_stunde.get_rect(center=(240, 80))

    schrift_minute = font.render(aufgabe_für_minute, True, (255, 255, 255))
    ausgabe_minute = schrift_minute.get_rect(center=(240, 240))


    bildschirm.fill((0, 0, 0)) 
    bildschirm.blit(schrift_stunde, ausgabe_stunde)
    bildschirm.blit(schrift_minute, ausgabe_minute)

    pygame.display.flip()
    sleep(5)

pygame.quit()
sys.exit()
