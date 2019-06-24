from pygame.time import get_ticks
from bullet import Bullet
from sprite import Sprite
from os import path


class Weapon:

    def __init__(self, weapon_sprite, bullet_sprite, max_ammo, damage, cool_down, reload_time):
        self.weapon_sprite = weapon_sprite
        self.bullet_sprite = bullet_sprite

        self.max_ammo = max_ammo
        self.damage = damage
        self.cool_down = cool_down * 1000
        self.reload_time = reload_time * 1000

        self.last_fire = get_ticks()

    def fire(self, x, y, dx, dy):
        self.last_fire = get_ticks()
        return Bullet(self.bullet_sprite, self.damage, x, y, dx, dy)
    
    def is_ready(self):
        return get_ticks() - self.last_fire >= self.cool_down

    def draw(self, surface, x, y):
        self.sprite.draw(surface, x, y)

    def rotate(self, angle):
        self.sprite.rotate(angle)


class MachineGun(Weapon):

    def __init__(self, width, height):
        # TODO: work on this

        sprite = Sprite(os.path.join('Weapons', 'MachineGun.png'), width, height)
        super().__init__(sprite, 35, 5, 0.1125, 3)
    