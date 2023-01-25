import pygame
from pygame.locals import *

pygame.init()

screen_width=1200
Screen_height=600

screen =pygame.display.set_mode((screen_width,Screen_height))
pygame.display.set_caption('platformer')

#define game variables
tile_size= 200

#load images
bg_img = pygame.image.load(r'sun.png')
sun_img = pygame.image.load(r'sky.png')



class world():
     

     def ___init__(self, data):
          self.tile_list =[]
          dirt_img = pygame.image.load('img/dirt.png')

          for row in data:
               col_count = 0
               for tile in row:
                    if tile == 1:
                         img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                         img_rect = img.get_rect()
                         img_rect.x = col_count = tile_size
                         img_rect.y = row_count = tile_size
                         tile =(img, img_rect)
                         self.title_list.append(tile)
                    col_count += 1     
               row_count += 1



world_data=[
[1, 1, 1, 1, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 1, 1, 1, 1],
]

world

run = True
while run:

     
     screen.blit(sun_img, (0,0))
     screen.blit(bg_img, (0,0))


     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
     pygame.display.update()
pygame.quit()



