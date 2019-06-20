from entity import Entity, TurnDirection
from animator import Animator

class Player(Entity):

    def __init__(self, controls, x, y, player_colour):
        super().__init__(x, y, Animator(player_colour))
        self.controls = controls

    def on_key_press(self, key):
        if self.controls['forward'] == key:
            self.speed = 5
        
        elif self.controls['back'] == key:
            self.speed -= 3
            
        elif self.controls['left'] == key:
            self.turn_direction = TurnDirection.LEFT

        elif self.controls['right'] == key:
            self.turn_direction = TurnDirection.RIGHT

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
        


