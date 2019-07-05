import pygame
from state import GameState
from setup import GameSetup
from game import GamePlay


pygame.init()
pygame.font.init()

display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Tank 2.0')

surface_width = display_surface.get_width()
surface_height = display_surface.get_height()
surface_background = [240, 155, 96]

done = False
clock = pygame.time.Clock()

game_state = GameState.SETUP

game_setup = GameSetup(None, display_surface)
game_play = GamePlay(None, surface_width, surface_height, None, None)

window = game_setup

while not done: # main game loop
    # pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
        
        # key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

            window.key_press(event.key)

        # key releases
        elif event.type == pygame.KEYUP:
            window.key_release(event.key)
        
        # click
        elif event.type == pygame.MOUSEBUTTONUP:
            window.click(event.button, pygame.mouse.get_pos())
            window = game_play

    display_surface.fill(surface_background)

    
    window.render(display_surface)
    pygame.display.flip()
    clock.tick(120)

pygame.quit()
