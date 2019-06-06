import pygame
import sprite
from animator import Animator

pygame.init()
display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Elemental TPS')

surface_width = display_surface.get_width()
surface_height = display_surface.get_height()
surface_background = [240, 155, 96]

done = False

clock = pygame.time.Clock()

while not done: # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break

    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_ESCAPE]:
        done = True
    
    display_surface.fill(surface_background)

    # game 

    pygame.display.flip()

    # update limiter
    clock.tick(1000 / 60)
    

pygame.quit()
exit()

