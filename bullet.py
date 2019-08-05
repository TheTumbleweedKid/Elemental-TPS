from sprite import Sprite
from entity import Entity, TurnDirection
from main import surface_width, surface_height
from os import path


class Bullet(Entity):

    def __init__(self, player, calibre, damage, x, y, rotation, speed, width, height):
        sprite_path = path.join('Bullets', calibre + '.png')
        super().__init__(x, y, Sprite(sprite_path), speed=speed)

        self.damage = damage
        self.player = player

        self.width = width
        self.height = height

        self.x = x
        self.y = y

        self.rotation = rotation

        self.sprite.rotate(self.rotation)

    def draw(self, surface):
        self.sprite.draw(surface, self.x, self.y)
    
    
    def is_touching(self, player):
        if (self.x >= player.x) and ((self.x + self.width) <= (player.x + player.width)) and (self.y >= player.y) and ((self.y + self.height) <= (player.y + player.height)): 
            player.health -= self.damage
            return True

    def should_remove(self, player):
        if self.is_touching(player) or (self.x > surface_width) or (self.x < 0) or (self.y > surface_height) or (self.y < 0):
            return True
    