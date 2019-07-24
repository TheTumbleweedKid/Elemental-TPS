import pygame
from player import Player

class GamePlay:

    def __init__(self, callback, window_width, window_height, class_1, class_2):
        self.callback = callback

        player1_controls = {
            'forward': pygame.K_UP,
            'back': pygame.K_DOWN,
            'left': pygame.K_LEFT,
            'right': pygame.K_RIGHT
        }

        player2_controls = {
            'forward': pygame.K_w,
            'back': pygame.K_s,
            'left': pygame.K_a,
            'right': pygame.K_d
        }

        self.player1 = Player(player1_controls, 80, 80, "Green", 100)
        self.player2 = Player(player2_controls, window_width - 240, window_height - 240, "Red", 100)
    

    def update(self, key):
        self.player1.update()
        self.player2.update()
    

    def render(self, surface):
        self.update(None)
        self.player1.draw(surface)
        self.player2.draw(surface)


    def key_press(self, key):
        self.player1.on_key_press(key)
        self.player2.on_key_press(key)
    

    def key_release(self, key):
        self.player1.on_key_release(key)
        self.player2.on_key_release(key)
    

    def click(self, button, pos):
        pass