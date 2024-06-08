
import pygame
from pygame.locals import *



class Constants:
    def __init__(self):
        self.SCREENWIDTH = 1200
        self.SCREENHEIGHT = 650
        self.GREY = (191, 191, 189)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BG_GREEN = (0, 28, 13)
        self.GREEN = (0, 255, 0)

class GameConstants:
    def __init__(self):
        self.SCREEN = None
        self.BOARD = None
        self.SUBOARD = None
        self.DRAW_SPACE = None


class Sprite:
    def __init__(self, img_name):
        self.img=pygame.image.load(img_name)
        self.rect_ver= None


class Buttons:
    def __init__(self):
        self.BANNER= None
        self.SAVE=None
        self.THIN_LINE= None
        self.DARK_COLOR= None


        self.LIGHT_COLOR= None    
        self.THICK_LINE = None

        self.DARK_MODE = None
        self.LIGHT_MODE = None
        self.HOW_TO = None

drawcolor = [255,255,255]
drawing = False
last_pos = None
thiccness = 1
fillcolor = (0,0,0)


#the basemaker creates various objects, it only exists to make the code less clunky
def BaseMaker(a,b):
    b.SCREEN=pygame.display.set_mode((a.SCREENWIDTH, a.SCREENHEIGHT))
    b.SCREEN.fill((a.BLACK))
    b.DRAW_SPACE=pygame.Rect(200, 100, 1000, 550)
    b.BOARD = pygame.draw.rect(b.SCREEN, a.BLACK, (200, 0, a.SCREENWIDTH, a.SCREENHEIGHT))
    b.SUBOARD = b.SCREEN.subsurface(b.DRAW_SPACE)  
 
    return b.SCREEN, b.BOARD, b.SUBOARD

#creates sprites
def ButtonCreator(c):
    c.BANNER=Sprite("banner.png")
    c.HOW_TO=Sprite("how_to.png")
    c.DARK_COLOR=Sprite("d_color.png")
    c.LIGHT_COLOR=Sprite("l_color.png")
    c.SAVE=Sprite("save.png")
    c.DARK_MODE=Sprite("d_mode.png")
    c.LIGHT_MODE=Sprite("l_mode.png")
    c.THICK_LINE=Sprite("thick_line.png")
    c.THIN_LINE=Sprite("thin_line.png")




#blits the menu, buttons and rectangles whenever necessary

def BoardBlitter(a,b,c):
    SIDE_BORDER = pygame.draw.rect(b.SCREEN, a.BLACK, (0, 0, 200, 650))
    UP_BORDER = pygame.draw.rect(b.SCREEN, a.BLACK, (0, 0, 1200, 100))

    SIDE_LINE = pygame.draw.line(b.SCREEN, a.GREEN, (200, 0), (200, 650))
    UP_LINE = pygame.draw.line(b.SCREEN, a.GREEN, (0, 100), (1200, 100))
    b.SCREEN.blit(c.BANNER.img, (0, 0))
    b.SCREEN.blit(c.HOW_TO.img, (600, 0))

    c.DARK_COLOR.rect_ver= pygame.draw.rect(b.SCREEN, a.GREEN, (25, 125, 150, 50))
    b.SCREEN.blit(c.DARK_COLOR.img,(25,125))



    c.LIGHT_COLOR.rect_ver=   pygame.draw.rect(b.SCREEN, a.GREEN, (25, 200, 150, 50))
    b.SCREEN.blit(c.LIGHT_COLOR.img, (25, 200))

    c.SAVE.rect_ver=   pygame.draw.rect(b.SCREEN, a.GREEN, (25, 275, 150, 50))
    b.SCREEN.blit(c.SAVE.img, (25, 275))


    c.DARK_MODE.rect_ver=pygame.draw.rect(b.SCREEN, a.GREEN, (25, 350, 150, 50))
    b.SCREEN.blit(c.DARK_MODE.img, (25, 350))

    c.LIGHT_MODE.rect_ver=pygame.draw.rect(b.SCREEN, a.GREEN, (25, 425, 150, 50))
    b.SCREEN.blit(c.LIGHT_MODE.img, (25, 425))


    c.THICK_LINE.rect_ver=pygame.draw.rect(b.SCREEN, a.GREEN, (25, 500, 150, 50))
    b.SCREEN.blit(c.THICK_LINE.img, (25, 500))

    c.THIN_LINE.rect_ver=pygame.draw.rect(b.SCREEN, a.GREEN, (25, 575, 150, 50))
    b.SCREEN.blit(c.THIN_LINE.img, (25, 575))
    

    pygame.display.update()