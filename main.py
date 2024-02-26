"""

To run this project you need pygame (pip3 install pygame) andyou need pytmx (pip3 install pytmx)
Comment every piece of code that you've done
Comment only in english pls
Have fun!


Folder:

Asset: all the imgaes an asset that we will use will be in there
Core: Mains files of the porject
Util: Utilis class and function that we will use 


Files:

main.py: main file
entity.py: all entity class will be in there
d

TODO list:

[!]: Collision with map border

[+]: Collision with wall

[-]: Ennemies
[-]: Weapon
[-]: Game play
[-]: Images
[-]: Level sys


Legend:

[!]: Very important
[+]: Important
[-]: Not very important

"""

# Main module
import pygame

# Other files needed
import Util.config as conf
import Util.entity as entity
import Util.camera as cam
import Util.screen as screen
import Util.tile as tile

# Other module
from random import randint
from sys import exit
from pytmx.util_pygame import load_pygame

pygame.init()

# Set up variables
class Game:
  def __init__(self):
    # Screen
    self.screen = pygame.display.set_mode(screen.WIN.size)
    pygame.display.set_caption(screen.WIN.caption)

    # Map
    self.tmx_data = load_pygame("Project/Asset/Map/RPG.tmx")

    # Game clock
    self.clock = pygame.time.Clock()
  
  # Function while the game is running
  def run(self):
    # Initialize the camera
    camera_group = cam.Camera((self.tmx_data.width,self.tmx_data.height)) # Contain all element on the screen
    
    # Initialize the player into the camera group
    player = entity.Player((50,200), camera_group, 100, 1, 0)

    # Add the test box into the screen
    """for i in range(12):
      random_pos = pygame.math.Vector2()
      random_pos.x = randint(0, screen.WIN.width)
      random_pos.y = randint(0, screen.WIN.height)

      entity.Box((random_pos.x,random_pos.y),camera_group)"""
    
    # Get info to print the tilemap ont the screen
    for layer in self.tmx_data.visible_layers:
      if hasattr(layer,'data'):
          for x,y,surf in layer.tiles():
            pos = (x * conf.TILE_SIZE.x, y * conf.TILE_SIZE.y)
            tile.Tile(pos = pos, surf = surf, group = camera_group).groups()

    # Game loop
    run = True
    while run:
      
      # Event loop
      for event in pygame.event.get():

        # If user quit
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()

      # Display the elements on the screen
      camera_group.custom_draw(player)
      camera_group.update()

      # Update the display of the window
      pygame.display.update()
      self.clock.tick(60) # FPS 

if __name__ == "__main__":
  game = Game()
  game.run()