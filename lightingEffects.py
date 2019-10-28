import pygame
import sys

screen=pygame.display.set_mode((640, 480))
light=pygame.image.load('circle.png') # radial gradient used for light pattern

light=pygame.transform.scale(light, (800,800)) # resize gradient

night = True # boolean to set if it is night or day

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
            break

    pos = []
    pos = pygame.mouse.get_pos() # get mouse position

    screen.fill(pygame.color.Color('White')) # just a background

    if night: 
        filter = pygame.surface.Surface((640, 480)) # create surface same size as window
        filter.fill(pygame.color.Color('Black')) # Black will give dark unlit areas, Grey will give you a fog
        filter.blit(light,(pos[0]-400,pos[1]-400)) # blit light to the filter surface -400 is to center effect
        screen.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_MIN) # blit filter surface but with a blend


    pygame.display.flip()
