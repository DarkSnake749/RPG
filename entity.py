import math
import pygame

# Player class
class Player(pygame.sprite.Sprite):
   def __init__(self, pos, group, health, lvl, xp):
        super().__init__(group)

        # Id
        self.name = "player"

        #health
        self.health = health

        #xp and level
        self.level = lvl
        self.xp = xp

        # Style of the player
        self.image = pygame.image.load("Project/Asset/Tiles/TX Player.png").convert_alpha()
        """self.image = pygame.Surface((50,50))
        self.image.fill("white")"""

        # Collision of the player
        self.rect = self.image.get_rect(center = pos) # Initial position (50, 200)

        # Mouvement direction (x,y)
        self.direction = pygame.math.Vector2()

        # Movement speed
        self.speed = 50
    
   # Movement function
   def dir(self):
      # Get all the key pressed
      keys = pygame.key.get_pressed()

      # Set the direction for what key is pressed
      if keys[pygame.K_w]: self.direction.y = -1  # Up
      elif keys[pygame.K_s]: self.direction.y = 1 # Down
      else: self.direction.y = 0                  # Don't move on Y
      if keys[pygame.K_a]: self.direction.x = -1  # Left
      elif keys[pygame.K_d]: self.direction.x = 1 # Right
      else: self.direction.x = 0                  # Don't move on X

      if self.direction.y and self.direction.x:   # Diagonal
         self.direction.y *= math.sqrt(0.5)
         self.direction.x *= math.sqrt(0.5)
   
   # Move in the appropriate direction
   def move(self): 
      self.rect.center += self.direction * self.speed
    
   # Collision
   def collision(self):
       
       # For each sprite on the screen
       for sprite in pygame.sprite.Sprite.groups(self)[0].sprites():
          
          # Continue if the sprite is not an obstacle
          if sprite.name != "box": continue

          # If the obstacle is a box
          elif sprite.name == "box":
             
             # If the player is acutally touching the target box 
             if pygame.Rect.colliderect(self.rect, sprite.rect):
                # Calculating the distance between the center of the player and the center of the box
                distacne = pygame.math.Vector2()
                distacne.y = self.rect.centery - sprite.rect.centery 

                # Collision from front
                if distacne.y <= 5 and not distacne.y < 0 and self.direction.y < 0: 
                   self.direction.y = 0
               
               # Collision from back
                elif distacne.y >= -5 and not distacne.y > 0 and self.direction.y > 0:
                   self.direction.y = 0

   # Update function
   def update(self):
       self.collision()
       self.move()
       self.dir()

"""class Box(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        # To id the box
        self.name = "box"
        
        # Style of the box
        self.image = pygame.Surface((48,70))
        self.image.fill("blue")

        # The collision box of the box
        self.rect = self.image.get_rect(topleft = pos)"""