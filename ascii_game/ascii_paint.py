import pygame
from pygame.locals import *
import tkinter as tk
from ascii_skeleton import BaseMaker,  ButtonCreator, BoardBlitter, Constants, GameConstants, Sprite, Buttons
from ascii_gameloop import mainloop

pygame.init()
pygame.display.set_caption("ASCII maker")
ROOT = tk.Tk()
ROOT.withdraw()

mode_color= (0,0,0)

a=Constants()
b=GameConstants()
c=Buttons()

BaseMaker(a,b)
ButtonCreator(c)
BoardBlitter(a,b,c)
ButtonCreator(c)
BoardBlitter(a,b,c)

mainloop(a,b,c)