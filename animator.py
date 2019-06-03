import os
from sprite import Sprite


class Animator:
    
    def __init__(self, name, width=20, height=20):
        self.frames = []
        self.index = 0
        self.ticks = 0

        self.path = os.path.join('assets', name)
        self.count = len(os.listdir(self.path))
        for i in range(0, self.count):
            self.frames.append(Sprite(os.path.join('explosion', '{}.png'.format(i)), width, height))

    def draw(self, surface, x, y):
        if not self.frames:
            return
        
        self.frames[self.index].draw(surface, x, y)

        self.ticks += 1
        if self.ticks > 20:
            self.ticks = 0
            self.index += 1

            if self.index >= len(self.frames):
                self.index = 0

    def rotate(self, angle):
        for frame in self.frames:
            frame.rotate(angle)