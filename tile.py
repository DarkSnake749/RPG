import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,surf,group):
        super().__init__(group)

        # Id
        self.name = "tile"

        # Basic info of the tile
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)