import pygame
import game_config as gc
from pygame import display, event, image
from animal import Animal
from time import sleep

def find_index(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return index

pygame.init()

display.set_caption("My Game")      #sets the window title
screen = display.set_mode((512, 512)) #sets the screen size; the function returns a surface object

matched = image.load('other_assets/matched.png')    #the image size if 512, do not need to resize
#screen.blit(matched, (0, 0))    #(0,0) is the starting coordinate of image
#display.flip()      # update the display

running = True      #indicates the game loop
tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]

current_images = [] #hold the last two images clicked

while running:
    current_events = event.get()    #this gives a list of all mouse and keyboard events
    for e in current_events:
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False

        if e.type == pygame.MOUSEBUTTONDOWN:    #get teh position of moues, so that index can be determined 
            mouse_x, mouse_y = pygame.mouse.get_pos()
            index = find_index(mouse_x, mouse_y)
            if index not in current_images:
                current_images.append(index)
            if len(current_images) > 2:
                current_images = current_images[1:] #forget the oldest image of 3 images
    
    screen.fill((255, 255, 255))

    total_skipped = 0

    for _, tile in enumerate(tiles):
        image_i = tile.image if tile.index in current_images else tile.box
        if not tile.skip:
            screen.blit(image_i, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))   #update the screen
        else:
            total_skipped += 1

    display.flip()
    
    if len(current_images) == 2:
        idx1, idx2 = current_images
        if tiles[idx1].name == tiles[idx2].name:
            tiles[idx1].skip = True
            tiles[idx2].skip = True
            sleep(0.4)
            screen.blit(matched, (0,0))
            display.flip()
            sleep(0.4)
            current_images = []

    if total_skipped == len(tiles):
        running = False

print('Goodbye!')