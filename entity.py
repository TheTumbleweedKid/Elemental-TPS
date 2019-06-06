import math

class Entity:

    def __init__(self, x, y, idle_animation, moving_animation):

        self.x = x
        self.y = y

        self.is_moving = False

        self.idle_animation = idle_animation
        self.moving_animation = moving_animation

        self.rotation = 0

    def draw(self, surface):
        if self.is_moving:
            self.moving_animation.draw(surface, self.x, self.y)
        
        else:
            self.idle_animation.draw(surface, self.x, self.y)

    def turn(self):
        