from entity import Entity, TurnDirection
from sprite import Sprite
from bullet import Bullet
from os import path
import time

class Player(Entity):

    def __init__(self, controls, x, y, player_colour, health=100):
        sprite_path = path.join('Players', player_colour + '.png')
        super().__init__(x, y, Sprite(sprite_path, 50, 50))
        self.controls = controls
        self.bullets = []
        self.last_fired = time.time()
        
        self.width = 50
        self.height = 50

        self.health = health

    def can_fire(self, delay):
        if time.time() - self.last_fired >= delay:
            return True

    def on_key_press(self, key):
        if self.controls['forward'] == key:
            self.speed += 2.5
        
        elif self.controls['back'] == key:
            self.speed -= 1.5
            
        elif self.controls['left'] == key:
            self.turn_direction = TurnDirection.LEFT

        elif self.controls['right'] == key:
            self.turn_direction = TurnDirection.RIGHT

        elif self.controls['fire'] == key:
            if self.can_fire(0.015):
                self.new_bullet = Bullet('.30', 15, self.x, self.y, self.rotation, 15, 20, 20)
                self.last_fired = time.time()
                self.bullets.append(self.new_bullet)

    def on_key_release(self, key):
        if self.controls['forward'] == key:
            if self.speed > 0:
                self.speed = 0

        elif self.controls['back'] == key:
            if self.speed < 0:
                self.speed = 0

        elif self.controls['left'] == key:
            if self.turn_direction == TurnDirection.LEFT:
                self.turn_direction = TurnDirection.NO_TURN

        elif self.controls['right'] == key:
            if self.turn_direction == TurnDirection.RIGHT:
                self.turn_direction = TurnDirection.NO_TURN

    


        


