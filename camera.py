import pygame
import Util.config as conf

# Camera class
class Camera(pygame.sprite.Group):
    def __init__(self,map_size): 
        super().__init__()
        
        # Id
        self.name = "cam"

        # Get the screen data
        self.display_surface = pygame.display.get_surface()

        # Map size
        self.map_size = map_size

        # Backdrop of the screen
        self.bd_surf = pygame.Surface((self.display_surface.get_size()))
        self.bd_surf.fill("black")
        self.bd_rect = self.bd_surf.get_rect(topleft = (0,0))

        # Get the background of the map
        self.bg_surf = pygame.Surface((map_size[0] * conf.TILE_SIZE.x, map_size[1] * conf.TILE_SIZE.y))
        self.bg_surf.fill("black")
        self.bg_rect = self.bg_surf.get_rect(topleft = (0,0))

        # Camera movement variables
        self.offset = pygame.math.Vector2()
        self.center_width = self.display_surface.get_size()[0] // 2
        self.center_height = self.display_surface.get_size()[1] // 2
    
    # Center the camera on the player
    def center_target(self, target):
        # Stop the offset to show the backdrop
        if target.rect.centerx - self.center_width > 0 and target.rect.centerx - self.center_width < (self.map_size[0] * conf.TILE_SIZE.x) - self.display_surface.get_size()[0]:
            self.offset.x = target.rect.centerx - self.center_width
        if target.rect.centery - self.center_height > 0 and target.rect.centery - self.center_height < (self.map_size[1] * conf.TILE_SIZE.y) - self.display_surface.get_size()[1]:
            self.offset.y = target.rect.centery - self.center_height
    
    # Custom draw to be more flexible with the display of the element of the screen
    def custom_draw(self, player):
        # Update the offset
        self.center_target(player)

        # Display the backdrop
        self.display_surface.blit(self.bd_surf,self.bd_rect)

        # Display the bg
        offset_pos = self.bg_rect.topleft - self.offset
        self.display_surface.blit(self.bg_surf,offset_pos)

        # Display the background
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            if sprite.name == "tile":
                self.display_surface.blit(sprite.image,offset_pos)

        # Blit each sorted sprite on the screen in order of y 
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            if sprite.name == "tile": continue
            offset_pos = sprite.rect.bottomleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
 