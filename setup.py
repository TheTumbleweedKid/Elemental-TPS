import pygame
from weapon import weapons


class GameSetup:

    def __init__(self, callback, surface):
        self.surface = surface
        self.callback = callback
        self.heading_font = pygame.font.SysFont('Bahnscrift', 40, True)
        self.button_font = pygame.font.SysFont('Bahnscrift', 40, True)
        self.setup_text = self.heading_font.render('Set up your players:', False, (100, 255, 255))
        self.buttons = []
        
        self.player1 = None
        self.player2 = None

        counter = 0
        for player in [self.player1, self.player2]:
            counter += 1
            weapon_counter = 0
            for weapon in weapons:
                weapon_counter += 1

                button_text = self.button_font.render(weapons[weapon]['name'], False, (100, 100, 100))
                new_button = Button(player, button_text, counter * 600, (weapon_counter * 100) + 50)

                self.buttons.append(new_button)

    def update(self, key):
        pass

    def render(self, surface):
        self.surface.blit(self.setup_text, (200, 200))
        for button in self.buttons:
            button.draw(surface)

    def key_press(self, key):
        pass
    
    def key_release(self, key):
        pass    

    def click(self, button, pos):
        print(pos)


class Button:

    def __init__(self, player, text, x, y, width=520, height=60):
        self.player = player
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_clicked(self, button, mouse_pos, x, y):
        pass
    
    def draw(self, surface):
        pygame.draw.rect(surface, (200, 200, 200), pygame.Rect(self.x - 60, self.y - 20, self.width, self.height))
        surface.blit(self.text, (self.x, self.y))