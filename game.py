import pygame
import sprite
from animator import Animator


pygame.init()
display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Elemental TPS')

surface_width = display_surface.get_width()
surface_height = display_surface.get_height()
surface_background = [240, 155, 96]

test_animation = Animator('explosion', width=200, height=200)

done = False

rotation = 0

while not done: # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break

    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_ESCAPE]:
        done = True
    
    display_surface.fill(surface_background)

    test_animation.draw(display_surface, 100, 100)
    test_animation.rotate(rotation)

    rotation += 1
    if rotation >= 360:
        rotation = 0

    pygame.display.flip()

pygame.quit()
exit()

