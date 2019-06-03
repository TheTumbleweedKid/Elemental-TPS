import pygame
import os


def rotate(surface, angle, pivot, offset):
    """Rotate the surface around the pivot point.

    Args:
        surface (pygame.Surface): The surface that is to be rotated.
        angle (float): Rotate by this angle.
        pivot (tuple, list, pygame.math.Vector2): The pivot point.
        offset (pygame.math.Vector2): This vector is added to the pivot.
    """
    rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
    rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect


class Sprite:

    def __init__(self, file_name, width=20, height=20):
        path = os.path.join(os.getcwd(), 'assets')
        
        self.original_image = pygame.image.load(os.path.join(path, file_name))
        self.original_image = pygame.transform.scale(self.original_image, (width, height))

        self.rotated_image = self.original_image
    
    def draw(self, surface, x, y):
        surface.blit(self.rotated_image, (x, y), (-50, -50, 50, 50))
        
    def rotate(self, angle):
        location = self.original_image.get_rect().center

        rotated_sprite = pygame.transform.rotate(self.original_image, angle)
        rotated_sprite.get_rect().center = (300, 30)

        print(rotated_sprite.get_rect().center)

        self.rotated_image = rotated_sprite

        #self.rotated_image = pygame.transform.rotate(self.original_image, angle)

        