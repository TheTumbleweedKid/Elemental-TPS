import os
from sprite import Sprite


class Animator:
    
    def __init__(self, name, width=40, height=40):

        self.frames = []
        self.index = 0
        self.ticks = 0

        self.path = os.path.join('assets', name)
        self.count = len(os.listdir(self.path))

        for i in range(0, self.count):
            frame_sprite = Sprite(os.path.join(name, '{}.png'.format(i)), width, height)
            self.frames.append(frame_sprite)

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