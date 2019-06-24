import math
from enum import Enum


class TurnDirection(Enum):
    LEFT = 1
    NO_TURN = 2
    RIGHT = 3


class Entity:

    def __init__(self, x, y, sprite, speed=0):
        self.speed = speed

        self.x = x
        self.y = y

        self.is_moving = True
        self.turn_direction = TurnDirection.NO_TURN

        self.sprite = sprite
        
        self.rotation = 0
        self.update_rotation()
    
    def update(self):
        if self.turn_direction == TurnDirection.LEFT:
            self.rotation += 3

        elif self.turn_direction == TurnDirection.RIGHT:
            self.rotation -= 3

        self.update_rotation()

        if self.is_moving:
            self.x += self.dx
            self.y += self.dy

    def draw(self, surface):
        self.sprite.draw(surface, self.x, self.y)

    def update_rotation(self):
        # check if rotation is less than 0 or greater than 360
        if self.rotation < 0:
            self.rotation += 360
            
        elif self.rotation > 360:
            self.rotation -= 360
        
        # rotate the animations
        self.sprite.rotate(self.rotation)

        radians = self.rotation * (math.pi / 180)

        self.dx = round(self.speed*math.sin(radians), 2)
        self.dy = round(self.speed*math.cos(radians), 2)