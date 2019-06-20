import pygame
from player import Player


pygame.init()
display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Elemental TPS')

surface_width = display_surface.get_width()
surface_height = display_surface.get_height()
surface_background = [240, 155, 96]

player1_controls = {
    'forward': pygame.K_UP,
    'back': pygame.K_DOWN,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT
}

player1 = Player(player1_controls, 80, 80, "Green")

done = False

clock = pygame.time.Clock()

while not done: # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
        
        # key presses
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

            player1.on_key_press(event.key)

        # key releases
        elif event.type == pygame.KEYUP:
            player1.on_key_release(event.key)
    
    # update
    player1.update()    
    
    # render
    display_surface.fill(surface_background)
    player1.draw(display_surface)
    pygame.display.flip()

    clock.tick(60)
    

pygame.quit()
