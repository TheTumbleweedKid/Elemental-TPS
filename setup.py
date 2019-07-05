import pygame


class GameSetup:

    def __init__(self, callback, surface):
        self.surface = surface
        self.callback = callback
        self.heading_font = pygame.font.SysFont('Bahnscrift', 40, True)
        self.setup_text = self.heading_font.render('Set up your players:', False, (100, 255, 255))
    
    def update(self, key):
        pass
    
    def render(self, surface):
        self.surface.blit(self.setup_text, (200, 200))

    def key_press(self, key):
        pass
    
    def key_release(self, key):
        pass
    
    def click(self, button, pos):
        print(pos)