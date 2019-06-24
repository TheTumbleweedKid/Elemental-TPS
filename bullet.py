class Bullet:

    def __init__(self, sprite, damage, x, y, dx, dy):
        self.sprite = sprite
        self.damage = damage

        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
    
    def draw(self, surface):
        self.sprite.draw(surface, x, y)
    
    def is_touching(self, player):
        # TODO: check if is touching player
        pass
    
    def should_remove(self):
        # TODO: check if the bullet has been around enough
        pass
    