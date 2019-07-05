from pygame.time import get_ticks
from bullet import Bullet
from sprite import Sprite
from os import path
from random import *
import json


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
    
    def ready_to_fire(self):
        return get_ticks() - self.last_fire >= self.cool_down

    def draw(self, surface, x, y):
        self.sprite.draw(surface, x, y)

    def rotate(self, angle):
        self.sprite.rotate(angle)


weapons = {
    'Sub-MachineGun': {
        'weapon_sprite': 'Sub-MachineGun.png',
        'bullet_sprite': 'Bullet.png',
        'damage': 3.25,
        'cool_down': 0.065,
        'spread': 0.65,
        'burst_size': 1,
        'burst_delay': 0,
        'max_ammo': 25,
        'reload_time': 2,
        'bullet_speed': 25,
        'player_acceleration': 2.5,
        'player_speed': 7
    },

    'MachineGun': {
        'weapon_sprite': 'MachineGun.png',
        'bullet_sprite': 'Bullet.png',
        'damage': 5.25,
        'cool_down': 0.1125,
        'spread': 0.19,
        'burst_size': 1,
        'burst_delay': 0,
        'max_ammo': 30,
        'reload_time': 2.5,
        'bullet_speed': 26,
        'player_acceleration': 2,
        'player_speed': 5.5
    },

    'HeavyMachineGun': {
        'weapon_sprite': 'HeavyMachineGun.png',
        'bullet_sprite': 'Bullet.png',
        'damage': 8,
        'cool_down': 0.2,
        'spread': 0.1,
        'burst_size': 1,
        'burst_delay': 0,
        'max_ammo': 65,
        'reload_time': 3.5,
        'bullet_speed': 25,
        'player_acceleration': 1.5,
        'player_speed': 4
    },

    'Sniper': {
        'weapon_sprite': 'Sniper.png',
        'bullet_sprite': 'Bullet.png',
        'damage': 35,
        'cool_down': 0.65,
        'spread': 0.075,
        'burst_size': 1,
        'burst_delay': 0,
        'max_ammo': 8,
        'reload_time': 3,
        'bullet_speed': 28,
        'player_acceleration': 2,
        'player_speed': 4.5
    },

    'HeavySniper': {
        'weapon_sprite': 'HeavySniper.png',
        'bullet_sprite': 'Bullet.png',
        'damage': 65,
        'cool_down': 1.25,
        'spread': 0,
        'burst_size': 1,
        'burst_delay': 0,
        'max_ammo': 5,
        'reload_time': 4,
        'bullet_speed': 28,
        'player_acceleration': 1.5,
        'player_speed': 4.5
    },

    'Random': {
        'weapon_sprite': 'Random.png',
        'bullet_sprite': 'Bullet.png',
        'damage': uniform(0.1, randint(55, 95)),
        'cool_down': uniform(0.01, 1.5),
        'spread': uniform(0, 3.0),
        'burst_size': randint(1, randint(1, randint(1, 2))),
        'burst_delay': 
            if burst_size > 1: 
                burst_delay = uniform(0.05, 0.25) 
            else:
                burst_delay = 0,
        'max_ammo': randint(13, 45),
        'reload_time': uniform(1.2, 4.75),
        'bullet_speed': uniform(15, 30),
        'player_acceleration': uniform(0.5, 4),
        'player_speed': uniform(4, 8)
    }

    
}