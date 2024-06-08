import os
import sys
import pygame
from pygame.locals import *
from tkinter import simpledialog
from PIL import Image
from ascii_skeleton import BoardBlitter


def mainloop(a,b,c):
    drawing = False
    mode_color= (0,0,0)
    drawcolor = [255,255,255]
    last_pos = None
    thiccness = 2
    fillcolor = (0,0,0)

    while True: #main gameloop
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():    #event handler loop
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN: 

                if pygame.mouse.get_pressed():  #if the mouse is down, the program looks for buttons pressed

                    #checks for a collidepoint between the click and the buttons

                    if pygame.Rect.collidepoint(c.DARK_COLOR.rect_ver, x, y):   #darkens the drawing color
                        if drawcolor[0]!=0 and drawcolor[1]!=0 and drawcolor[2]!=0:
                            drawcolor[0]= drawcolor[0]-5
                            drawcolor[1]= drawcolor[1]-5
                            drawcolor[2]= drawcolor[2]-5

                    if pygame.Rect.collidepoint(c.LIGHT_COLOR.rect_ver, x, y):  #lightens the drawing color
                        if drawcolor[0]!=255 and drawcolor[1]!=255 and drawcolor[2]!=255:
                            drawcolor[0]= drawcolor[0]+5
                            drawcolor[1]= drawcolor[1]+5
                            drawcolor[2]= drawcolor[2]+5

                    if pygame.Rect.collidepoint(c.THICK_LINE.rect_ver, x, y):   #thickens the line
                        thiccness = thiccness + 1
                    if pygame.Rect.collidepoint(c.THIN_LINE.rect_ver, x, y):    #thins the line
                        if thiccness>1:
                            thiccness = thiccness - 1

                    #saves the drawing:

                    if pygame.Rect.collidepoint(c.SAVE.rect_ver, x, y):
                        FILE_NAME = simpledialog.askstring(title="Save", prompt="Name of file?")
                        pygame.draw.line(b.SCREEN, mode_color, (200, 0), (200, 650))
                        pygame.draw.line(b.SCREEN, mode_color, (0, 100), (1200, 100))
                        pygame.image.save(b.SUBOARD, f"{FILE_NAME}.jpg")

                        script_dir = os.path.dirname(__file__)  #finds the directory of the program
                        rel_path = f"{FILE_NAME}.jpg"   #names it
                        abs_file_path = os.path.join(script_dir, rel_path)  #creates absolute path

                        #resizing the image and making it back and white:
                        # (it is necessary to make the image tiny because one ascii character is going to be one pixel)

                        img = Image.open(abs_file_path)
                        width, height = img.size
                        aspect_ratio = height / width
                        new_width = 150
                        new_height = aspect_ratio * new_width * 0.5
                        img = img.resize((new_width, int(new_height)))
                        img = img.convert('L')
                        pixels = img.getdata()

                        #in light mode, the drawing is made of "empty" spaces and vice versa in dark mode

                        for i in range(len(pixels)):    #gets pixels and assigns ascii character based on rgb values
                            print(pixels[i])
                        DARKMODE = True
                        LIGHT_CHARS = ["@", "$", "&", "#", "B", "%", "S", "*", ":", ".", " "]
                        DARK_CHARS = [" ", ".", ":", "*", "S", "%", "B", "#", "&", "$", "@"]

                        if DARKMODE is True:
                            new_pixels = [DARK_CHARS[pixel // 25] for pixel in pixels]
                        else:
                            new_pixels = [LIGHT_CHARS[pixel // 25] for pixel in pixels]

                        new_pixels = ''.join(new_pixels)
                        new_pixels_count = len(new_pixels)
                        ascii_image = []

                        for index in range(0, new_pixels_count, img.width):
                            ascii_image.append(new_pixels[index:index + img.width])
                        ascii_image = "\n".join(ascii_image)

                        file = FILE_NAME + ".txt"
                        with open(file, "w") as f:
                            f.write(ascii_image)
                            
                    #changes modes

                    if pygame.Rect.collidepoint(c.DARK_MODE.rect_ver, x, y):
                        fillcolor= a.BLACK
                        b.SCREEN.fill(fillcolor)
                        drawcolor=[255,255,255]
                        BoardBlitter(a,b,c)

                    if pygame.Rect.collidepoint(c.LIGHT_MODE.rect_ver, x, y):
                        fillcolor= a.WHITE
                        b.SCREEN.fill(fillcolor)
                        drawcolor=(0,0,0)
                        BoardBlitter(a,b,c)

            if event.type == MOUSEBUTTONDOWN:
                drawing = True
            if event.type == MOUSEMOTION:
                # draws continous line if the mouse button is down
                if drawing == True:
                    mouse_position = pygame.mouse.get_pos()
                    if last_pos is not None:
                        pygame.draw.line(b.SCREEN, drawcolor, last_pos, mouse_position, thiccness)
                        BoardBlitter(a,b,c)
                        pygame.display.update()
                    last_pos = mouse_position

            # resets all values if mouse is not down
            if event.type == MOUSEBUTTONUP:
                
                mouse_position = (0, 0)
                drawing = False
                last_pos = None
