# paint.py
# Saad Ahmed

# The title pretty much explains the program. Basically something
# similar to Microsoft Paint, give or take a few tool options.

# USING THE PROGRAM

# Right click clears screen
# Middle mouse click shows colour palette
# other tool options are given in the grey box under the canvas


# basic set up for any program
from pygame import *
from random import *
init()
screen = display.set_mode((1024, 668))
title = display.set_caption("The Awesomes Character Predictor")


canvas = Rect(102, 52, 664, 614) # main canvas
bcanvas = Rect (100, 50, 668, 618) # border around canvas 
running = True
currtool = "" # current tool
sub = screen.subsurface(canvas) # a subsurface for the canvas

# text size for text tool
tsize = 12

# some common colours
white = 255, 255, 255
black = 0, 0, 0
blue = 0, 0, 255
green = 0, 255, 0
red = 255, 0, 0
purple = 255, 0, 255
dgreen = 0, 200, 0

# radii for paint and eraser
radiuspaint = 20
radiuseraser = 20

# load palette + background image
palette = image.load ("pics/spectrum.jpg")
paletteback = image.load("pics/palettebacknew.jpg") # background for palette

back = image.load("pics/backgroundnew.jpg")

# load music
#music = mixer.music.load("London.mp3")

# stamp lists
bstamps = []
sstamps = []
srects = []
spot = []

# buttons
buttonpics = [("buttons/norm1.jpg", "buttons/hover1.jpg", "buttons/press1.jpg"),
              ("buttons/norm2.jpg", "buttons/hover2.jpg", "buttons/press2.jpg"),
              ("buttons/norm3.jpg", "buttons/hover3.jpg", "buttons/press3.jpg"),
              ("buttons/norm4.jpg", "buttons/hover4.jpg", "buttons/press4.jpg"),
              ("buttons/norm5.jpg", "buttons/hover5.jpg", "buttons/press5.jpg"),
              ("buttons/norm6.jpg", "buttons/hover6.jpg", "buttons/press6.jpg"),
              ("buttons/norm7.jpg", "buttons/hover7.jpg", "buttons/press7.jpg"),
              ("buttons/norm8.jpg", "buttons/hover8.jpg", "buttons/press8.jpg"),
              ("buttons/norm9.jpg", "buttons/hover9.jpg", "buttons/press9.jpg"),
              ("buttons/norm10.jpg", "buttons/hover10.jpg", "buttons/press10.jpg"),]

# load load/save buttons
loadn = image.load("buttons/loadnorm.jpg")
loadp = image.load("buttons/loadpress.jpg")
saven = image.load("buttons/savenorm.jpg")
savep = image.load("buttons/savepress.jpg")
loadsaves = [loadn, loadp, saven, savep]
alphals = 100 # load/save button alphas
loadsaverect = Rect(540, 0, 200, 50) # ret containg load/save buttons

button = []
cbutton = []

currbuttoncol = [0]*10  # curr. button colour
buttoncols = [blue] * 10 # button border colours
buttonthicks = [1] * 10 # button thicknesses (borders)
trans = 255 # stamp transparency

# nested for loop for buttons
for f in range(10):   # each tools button's
        for s in range(3):  # each button's three colour types
                cbutton.append(image.load(buttonpics[f][s]))
        button.append(cbutton)
        cbutton = []

# make list of stamps and stamp previews(smaller)
bpics = ("bpics/bs1.jpg", "bpics/bs2.jpg", "bpics/bs3.jpg", "bpics/bs4.jpg",
         "bpics/bs5.jpg", "bpics/bs6.jpg", "bpics/bs7.jpg", "bpics/bs8.jpg",
         "bpics/bs9.jpg", "bpics/bs10.jpg", "bpics/bs11.jpg")
spics = ("spics/ss1.jpg", "spics/ss2.jpg", "spics/ss3.jpg", "spics/ss4.jpg",
         "spics/ss5.jpg", "spics/ss6.jpg", "spics/ss7.jpg", "spics/ss8.jpg",
         "spics/ss9.jpg", "spics/ss10.jpg", "spics/ss11.jpg")

num_stamps = len(spics) # get number of stamps

# load stamps
for i in range (num_stamps):
        bstamps.append(image.load (bpics[i])) # stamps
        sstamps.append(image.load (spics[i])) # stamp previews
        spot.append(i*57)  # a spot for each stamp preview
        srects.append(Rect(805, spot[i], 100, 53)) # rectangle on the spot of each preview
current = bstamps[1] # spot of currently selected stamp
currentspot = 1 # currently selected stamp
stamps = Rect (800, 50, 100, 570) # the whole space that the stamps are located inside
         
# palette objects/variables
paletteborder = Rect(120, 150, 670, 410) # black border around canvas
cancel = Rect(140, 530, 40, 20) # cancel button for palette
select = Rect(200, 530, 40, 20) # select button for palette
palettebox = Rect(130, 180, 600, 345)  # main palette
newcol = (0, 0, 0) # new colour chosen by palette (currently black)
pnx, pny = 0, 0 # palette positions (where person chooses colour)
paletterect = Rect(130, 180, 600, 345) # palette border

# fonts/messages
info_message = ""    # info about which tool you are currently hovering over
selected_message = "None" # the current selected tool
font = font.SysFont("Times New Roman", 18)
toolinfobox = Rect(100, 580, 700, 40) # grey box under canvas

# tool boxes
pencilt = Rect (0, 50, 50, 50)
erasert = Rect (50, 50, 49, 50)
sprayt = Rect (0, 100, 50, 50)
linet = Rect (50, 100, 49, 50)
paintt = Rect (0, 150, 50, 50)
stampt = Rect (50, 150, 49, 50)
shapet = Rect (0, 200, 50, 50)
effectt = Rect (50, 200, 49, 50)
eyedroppert = Rect (0, 250, 50, 50)
polyt = Rect (50, 250, 49, 50)
buttons = Rect (0, 50, 100, 250)
savet = Rect (540, 5, 90, 35)
loadt = Rect (650, 5, 90, 35)


# current colour box
colourbox = Rect(34, 639, 37, 37)

# R, B, G sliders
Rbox = Rect (200, 633, 510, 14)
Bbox = Rect (200, 653, 510, 14)
Gbox = Rect (200, 673, 510, 14)
Rslider = 200
Bslider = 200
Gslider = 200

# spray paint sliders
radslider = 540
sizeslider = 540

# polygon list
pts = []  # points for drawing polygon
polythick = 1
new = [screen.copy()]*2 # make two copies (one for drawing polygon, one after it's drawn)

# drawing the main canvas
draw.rect (screen, (white), canvas)
subc = sub.copy() # canvas copy

# play music in background
#mixer.music.play(0)

# shapetool objects
shapetool = ""
squarecol = 100, 100, 100 # colour of tool button
circlecol = 100, 100, 100
squarerect = Rect(15, 370, 70, 70) # rects containing buttons
circlerect = Rect(15, 450, 70, 70)

# effect tool objects
effectbox = Rect (10, 400, 70, 70) # effects button
efchooseb = Rect (120, 150, 670, 410) # choosing effects box
efcancel = Rect(140, 530, 40, 20)# cancel choose effect box
efselect = Rect(200, 530, 40, 20) # select effect box
efcol = [(100, 100, 100)] * 9 # current effect box colour (tells which is selected)
effectback = image.load("pics/effectback.jpg")

# boxes for each effect
bwbox = Rect (140, 170, 100, 50)
invbox = Rect (140, 240, 100, 50)
brbox = Rect (140, 310, 100, 50)
darkbox = Rect (140, 380, 100, 50)
funkybox = Rect (200, 450, 100, 50)
negbox = Rect (260, 170, 100, 50)
redbox = Rect (260, 240, 100, 50)
greenbox = Rect (260, 310, 100, 50)
bluebox = Rect (260, 380, 100, 50)

neftype = "b and w" # temp. variable for choosing effect
eftype = "b and w" # which effect is currently selected

#################################  FUNCTIONS  ################################## 

# Load function
def load():
        global copy
        filename = raw_input("enter the name you would like to load (do not include extension)")
        try: # try loading file that user has entered
                loaded = image.load("saved/" + filename + ".jpg")
                screen.blit(loaded, (canvas))
                copy = screen.copy()
                print "file loaded!"
        except: 
                print "invalid filename"

# Save function     
def save():
        global subc
        filename="test"
        image.save(subc, (filename + ".jpg"))
        print "Predicting..."


# drawing save/load buttons
def drawsv():
        global savet, loadt
        draw.rect (screen, (100, 100, 100), savet, 1)
        draw.rect (screen, (100, 100, 100), loadt, 1)



# drawing the buttons
def drawbuttons():
        global alphals, buttonthicks, buttoncols, button, currbuttoncol, pencilt, erasert, sprayt, linet, paint, stampt, squaret, circlet, eyedroppert, mx, my, currtool

        
        for i in range (4):
                loadsaves[i].set_alpha(alphals)
        alphals = 100
        if loadsaverect.collidepoint(mx, my):
                alphals = 200
        screen.blit(loadn, (loadt))
        screen.blit(saven, (savet))
        
        
        for f in range(10): # alpha = 150 if mouse is not selecting tools
                for s in range(3):
                        button[f][s].set_alpha(150)
        
        if buttons.collidepoint(mx, my):
                for f in range(10): #alpha = 240 if mouse is selecting tools
                        for s in range(3):
                                button[f][s].set_alpha(240)
                
        screen.blit (button[0][currbuttoncol[0]], (1, 51))
        if currtool != "pencil":
                currbuttoncol[0] = 0 # change colour back to normal (same for ones below)
        draw.rect (screen, (buttoncols[0]), pencilt, buttonthicks[0])
        
        screen.blit (button[1][currbuttoncol[1]], (50, 51))
        if currtool != "eraser":
                currbuttoncol[1] = 0
        draw.rect (screen, (buttoncols[1]), erasert, buttonthicks[1])

        screen.blit (button[2][currbuttoncol[2]], (1, 101))
        if currtool != "spray":
                currbuttoncol[2] = 0
        draw.rect (screen, (buttoncols[2]), sprayt, buttonthicks[2])

        screen.blit (button[3][currbuttoncol[3]], (50, 101))
        if currtool != "line":
                currbuttoncol[3] = 0
        draw.rect (screen, (buttoncols[3]), linet, buttonthicks[3])

        screen.blit (button[4][currbuttoncol[4]], (1, 151))
        if currtool != "paintbr":
                currbuttoncol[4] = 0
        draw.rect (screen, (buttoncols[4]), paintt, buttonthicks[4])

        screen.blit (button[5][currbuttoncol[5]], (50, 151))
        if currtool != "stamp":
                currbuttoncol[5] = 0
        draw.rect (screen, (buttoncols[5]), stampt, buttonthicks[5])

        screen.blit (button[6][currbuttoncol[6]], (1, 201))
        if currtool != "shape":
                currbuttoncol[6] = 0
        draw.rect (screen, (buttoncols[6]), shapet, buttonthicks[6])

        screen.blit (button[7][currbuttoncol[7]], (50, 201))
        if currtool != "effect":
                currbuttoncol[7] = 0
        draw.rect (screen, (buttoncols[7]), effectt, buttonthicks[7])

        screen.blit (button[8][currbuttoncol[8]], (1, 251))
        if currtool != "eyedropper":
                currbuttoncol[8] = 0
        draw.rect (screen, (buttoncols[8]), eyedroppert, buttonthicks[8])

        screen.blit (button[9][currbuttoncol[9]], (50, 251))
        if currtool != "polygon":
                currbuttoncol[9] = 0
        draw.rect (screen, (buttoncols[9]), polyt, buttonthicks[9])
        
def tool_select():
        global mx, my, mb, currbuttoncol, info_message, buttoncols, buttonthicks, selected_message, currtool 
        if pencilt.collidepoint(mx, my):
                currbuttoncol[0] = 1
                info_message = "Pencil Tool: Use pencil to draw freestyle"
                buttoncols[0] = purple
                buttonthicks[0] = 2
                if mb[0] == 1:
                        selected_message = "Pencil"
                        currtool = "pencil"

        elif erasert.collidepoint(mx, my):
                currbuttoncol[1] = 1
                info_message = "Eraser Tool: Erase what you have drawn"
                buttoncols[1] = purple
                buttonthicks[1] = 2
                if mb[0] == 1:
                        selected_message = "Eraser: adjust size with up/down arrow keys"
                        currtool = "eraser"
                        
        elif sprayt.collidepoint (mx, my):
                currbuttoncol[2] = 1
                info_message = "Spray Tool: Thickness and radius adjustable"
                buttoncols[2] = purple
                buttonthicks[2] = 2
                if  mb[0] == 1:
                        selected_message = "Spray Paint: thickness and radius adjustable (sliders on the right)"
                        currtool = "spray"
                        
        elif linet.collidepoint(mx, my):
                currbuttoncol[3] = 1
                info_message = "Line Tool: Draw straight lines"
                buttoncols[3] = purple
                buttonthicks[3] = 2
                if mb[0] == 1:
                        selected_message = "Line: adjust thickness with up/down arrow keys while drawing"
                        currtool = "line"
                        
        elif paintt.collidepoint(mx, my):
                currbuttoncol[4] = 1
                info_message = "Paint Brush Tool: Use paint brush to draw freestyle"
                buttoncols[4] = purple
                buttonthicks[4] = 2
                if mb[0] == 1:
                        selected_message = "Paint Brush: adjust size with up/down arrow keys"
                        currtool = "paintbr"
                        
        elif stampt.collidepoint(mx, my):
                currbuttoncol[5] = 1
                info_message = "Stamp Tool: Stamp pictures from a seletion"
                buttoncols[5] = purple
                buttonthicks[5] = 2
                if mb[0] == 1:
                        selected_message = "Stamp: adjust transparency with up/down arrow keys"
                        currtool = "stamp"
                        
        elif shapet.collidepoint(mx, my):
                currbuttoncol[6] = 1
                info_message = "Shape tool: draw rectangles and circles"
                buttoncols[6] = purple
                buttonthicks[6] = 2
                if mb[0] == 1:
                        selected_message = "Shapes: Select a shape type from side"
                        currtool = "shape"
                        
        elif effectt.collidepoint(mx, my):
                currbuttoncol[7] = 1
                info_message = "Effect tool: add various effects to things on canvas"
                buttoncols[7] = purple
                buttonthicks[7] = 2
                if mb[0] == 1:
                        selected_message = "Effects: draw a rectangle on the place you want affected"
                        currtool = "effect"
                        
        elif eyedroppert.collidepoint(mx, my):
                currbuttoncol[8] = 1
                info_message = "Eyedropper Tool: Select a colour on the canvas"
                buttoncols[8] = purple
                buttonthicks[8] = 2
                if mb[0] == 1:
                        selected_message = "Eyedropper"
                        currtool = "eyedropper"

        elif polyt.collidepoint(mx, my):
                currbuttoncol[9] = 1
                info_message = "Polygon Tool: Make your own shape"
                buttoncols[9] = purple
                buttonthicks[9] = 2
                if mb[0] == 1:
                        selected_message = "Polygon: double click to set, up/down arrow keys adjust fill/thickness"
                        currtool = "polygon"

                        
# draw black border around canvas (temporary, not used anymore)
def draw_border():
        
        draw.polygon(screen, (black), [(0, 0), (0, 700), (900, 700), (900, 0),
                                       (100, 0), (100, 50), (800, 50), (800, 620),
                                       (100, 620), (100, 0)])

# drawing the background picture (replaced the prev. function for background)
def background():
        screen.blit(back, (0, 0))

def clrscreen(): # right click to clear screen
        global canvas, sub, subc, copy
        draw.rect(screen, (white), (canvas))
        subc = sub.copy()
        copy = screen.copy()

def col_choose ():
        
        global copy, Rslider, Bslider, Gslider, newcol, pnx, pny, c
        
        # background setup
        screen.blit (copy, (0, 0))
        paletteback.set_alpha(100)
        screen.blit (paletteback, (120, 150))
        draw.rect (screen, (255, 0, 0), cancel)
        draw.rect (screen, (0, 255, 0), select)
        
        draw.line (screen, (0, 150, 0), (205, 537), (210, 545), 2)
        draw.line (screen, (0, 150, 0), (210, 545), (235, 532), 2)
        draw.line (screen, (150, 0, 0), (145, 535), (175, 543), 2)
        draw.line (screen, (150, 0, 0), (145, 543), (175, 535), 2) 
        
        choosing = True
        
        while choosing:
                screen.set_clip()
                
                event.get()
                mb = mouse.get_pressed()
                mx, my = mouse.get_pos()

                # draw border ad colour box
                draw.rect (screen, (newcol), (740, 220, 40, 40))
                draw.rect (screen, (white), (740, 220, 40, 40), 1)
                draw.rect (screen, (50, 50, 50), (120, 150, 670, 410), 1)
                draw.rect (screen, (black), (129, 179, 602, 347), 1)

                # draw palette
                screen.set_clip(paletterect)
                screen.blit (palette, (130, 180))
                draw.circle (screen, (black), (pnx, pny), 8, 1)

                
                
                display.flip()

                # select colour
                if mb[0] == 1 and palettebox.collidepoint (mx, my):
                        pnx, pny = mx, my
                        newcol = screen.get_at((pnx, pny))

                if select.collidepoint (mx, my) and mb[0] == 1:
                        choosing = False
                        Rslider = newcol[0]*2+200
                        Gslider = newcol[1]*2+200
                        Bslider = newcol[2]*2+200
                        c = (newcol[0], newcol[1], newcol[2])
                if cancel.collidepoint (mx, my) and mb[0] == 1:
                        choosing = False
                

        # exit palette only when mousebutton is released from cancel/select
        # buttons, or else the eyedropper tool (if selected) will change
        # the colour to something else.
        while mb[0] == 1:
                event.pump()
                mb = mouse.get_pressed()
        screen.set_clip()
        screen.blit (copy, (0, 0)) # blits the prev. copy of screen
                                   # to make the palette go away

# spray paint tool
def spray(mx, my, radslider, sizeslider, c):
        rad = int((540 - radslider)/3) # set radius according to slider
        size = int((540 - sizeslider)/15) # set thickness according to slider
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        if mb[0] == 1 and canvas.collidepoint (mx, my):
                spraying = True
                while spraying: # in a loop so it goes faster
                        screen.set_clip(canvas)
                        event.get()
                        mx, my = mouse.get_pos()
                        mb = mouse.get_pressed()
                        for i in range(rad/(size+1)): # set a speed based on both size and radius (so it's not too fast or too slow)
                                x = randint(mx-rad, mx+rad)
                                y = randint(my-rad, my+rad)
                                if ((x-mx)**2 + (y-my)**2)**0.5 <= rad: # spray
                                        draw.circle (screen, (c), (x, y), size)
                        if mb [0] == 0:
                                spraying = False
                        display.flip()
        screen.set_clip()

# eraser tool
def erase (mx, my, copy, rad):
        mb = mouse.get_pressed()
        if canvas.collidepoint (mx, my):
                # draw eraser preview
                draw.circle (screen, (white), (mx, my), rad)
                draw.circle (screen, (black), (mx, my), rad, 1)
                display.flip()
                screen.blit(copy, (0, 0))
                if mb[0] == 1:
                        lastx, lasty = mx, my
                        erasing = True
                        while erasing:
                                screen.set_clip(canvas)
                                draw.circle (screen, (white), (mx, my), rad)
                                event.get()
                                mb = mouse.get_pressed()
                                mx, my = mouse.get_pos()
                                draw.line (screen, (white), (lastx, lasty), (mx, my), rad*2) # connect lines to make it smooth
                                display.flip()
                                lastx, lasty = mx, my
                                
                                if mb[0] == 0:
                                        erasing = False
        screen.set_clip()

# paint brush tool
def paint (mx, my, rad): # same as eraser but with different colours
        global copy, c, subc, sub
        mb = mouse.get_pressed()
        if canvas.collidepoint (mx, my):
                draw.circle (screen, (c), (mx, my), rad)
                if mb[0] == 1:
                        screen.set_clip(canvas)
                        draw.circle (screen, (c), (mx, my), rad)
                        lastx, lasty = mx, my
                        painting = True
                        while painting:
                                event.get()
                                mb = mouse.get_pressed()
                                mx, my = mouse.get_pos()
                                
                                draw.line (screen, (c), (lastx, lasty), (mx, my), rad*2)
                                draw.circle (screen, (c), (mx, my), rad)
                                display.flip()
                                lastx, lasty = mx, my
                                subc = sub.copy()
                                
                                
                                
                                if mb[0] == 0:
                                        painting = False
        
        screen.set_clip()

# line tool
def line (mx, my, c, copy):
        mb = mouse.get_pressed()
        linethick = 1
        if mb[0] == 1 and canvas.collidepoint(mx, my):
                lining = True
                while lining:
                        screen.set_clip(canvas)
                        event.get()
                        nb = mouse.get_pressed()
                        nx, ny = mouse.get_pos()
                        keys = key.get_pressed()
                        draw.line (screen, (c), (mx, my), (nx, ny), linethick)
                        if keys[K_UP]:
                                linethick+=.5
                                if linethick > 10:
                                        linethick = 10
                        if keys[K_DOWN]:
                                linethick-=.5
                                if linethick <1:
                                        linethick = 0

                        
                        display.flip()
                        screen.blit(copy, (0, 0))
                        copy = screen.copy()
                        
                        if nb[0] == 0:
                                lining = False
                event.get()
                nx, ny = mouse.get_pos()
                draw.line (screen, (c), (mx, my), (nx, ny), linethick)
        screen.set_clip()

# pencil/pen tool
def pencil(mx, my, c):
        mb = mouse.get_pressed()
        if mb[0] == 1 and canvas.collidepoint(mx, my):
                lastx, lasty = mx, my
                drawing = True
                while drawing:
                        screen.set_clip(canvas)
                        event.get()
                        mb = mouse.get_pressed()
                        mx, my = mouse.get_pos()
                        draw.line (screen, (c), (mx, my), (lastx, lasty))
                        display.flip()
                        lastx, lasty = mx, my
                        if mb[0] == 0:
                                drawing = False
        screen.set_clip()

# square/box tool
def square (mx, my, c, copy):
        squarethickness = 0
        mb = mouse.get_pressed()
        if mb[0] == 1 and canvas.collidepoint(mx, my):
                boxing = True
                while boxing:
                        screen.set_clip(canvas)
                        event.get()
                        keys = key.get_pressed()
                        
                        nb = mouse.get_pressed()
                        nx, ny = mouse.get_pos()
                        draw.rect (screen, (c), (mx, my, nx-mx, ny-my), squarethickness)
                        if keys[K_UP] == 1:
                                squarethickness+=0.5
                        if keys[K_DOWN] == 1:
                                squarethickness-= 0.5
                                if squarethickness < 1:
                                        squarethickness = 0
                        width = nx-mx
                        height = ny - my
                        
                        if squarethickness > width/2:
                                squarethickness = 0
                        if squarethickness > height/2:
                                squarethickness = 0
                        
                        display.flip()
                        screen.blit(copy, (0, 0))
                        copy = screen.copy()
                        
                        if nb[0] == 0:
                                boxing = False
                event.get()
                nx, ny = mouse.get_pos()
                draw.rect (screen, (c), (mx, my, nx-mx, ny-my), squarethickness)
        screen.set_clip()
        
# ellipse/circle tool
def circle (mx, my, c, copy):
        circlethickness = 0
        mb = mouse.get_pressed()
        if mb[0] == 1 and canvas.collidepoint(mx, my):
                circling = True
                while circling:
                        screen.set_clip(canvas)
                        event.get()
                        keys = key.get_pressed()
                        nb = mouse.get_pressed()
                        nx, ny = mouse.get_pos()
                        temp = Rect(mx, my, nx-mx, ny-my)
                        
                        
                        temp.normalize() # will prevent radius from going negative and crashing
                        draw.ellipse (screen, (c), temp, circlethickness)
                        if keys[K_UP] == 1: # adjust thickness while drawing
                                circlethickness+=0.5
                        if keys[K_DOWN] == 1:
                                circlethickness-= 0.5
                                if circlethickness < 1:
                                        circlethickness = 0
                        width = nx-mx
                        height = ny - my
                        if circlethickness > width/2:
                                circlethickness = 0
                        if circlethickness > height/2:
                                circlethickness = 0
                        
                        display.flip()
                        screen.blit(copy, (0, 0))
                        copy = screen.copy()
                        
                        if nb[0] == 0:
                                circling = False
                event.get()
                nx, ny = mouse.get_pos()
                draw.ellipse (screen, (c), temp, circlethickness)
        screen.set_clip()
        
# stamp tool
def stamp (mx, my, current,spot):
        global copy, sub, subc, trans
        stamping = True
        while stamping:
                for i in range (num_stamps):  # draw stamps in their current spots
                        sstamps[i].set_alpha(150) # make them transparent-ish
                        screen.blit (sstamps[i], (805, spot[i]))
                        draw.rect (screen, (0, 255, 0), (805, spot[currentspot], 90, 53), 2)
                        
                event.get()
                mx, my = mouse.get_pos()
                mb = mouse.get_pressed()
                keys = key.get_pressed()

                if mb[1] == 1:
                        col_choose()
                
                if keys[K_UP] == 1:
                        trans+=5
                        if trans>254:
                                trans = 255
                if keys[K_DOWN] == 1:
                        trans-= 5
                        if trans < 1:
                                trans = 3         

                screen.set_clip(canvas)
                display.flip()

                # blit copy so that the preview doesn't stay on the same spot
                screen.blit (copy, (0, 0))
                copy = screen.copy()
                
                screen.blit (current, (mx-175, my-102))
                current.set_alpha(trans)
                if mb[0] == 1:
                        copy = screen.copy()
                        
                        stamping= False
                if canvas.collidepoint (mx, my) == False:
                        stamping = False
                if mb[2] == 1:
                        clrscreen()

                display.flip()
                
        # wait for mouse to release before drawing new
        while mb[0] == 1:
                event.pump()
                mb = mouse.get_pressed()
                
        screen.blit (copy, (0, 0))
        screen.set_clip()
        subc = sub.copy()

# Text tool (not used) 
def text (mx, my, texts):
        global copy, c, subc, sub, fontt, tsize
        while canvas.collidepoint(mx, my):
                event.pump()
                mx,my = mouse.get_pos()
                mb = mouse.get_pressed()
                keys = key.get_pressed()
                if keys[K_UP] == 1:
                        tsize+=0.5
                if keys[K_DOWN] == 1:
                        tsize-= 0.5
                        if tsize < 1:
                                tsize = 1

                fontt = ("Ariel", tsize)
                words = font.render(texts, True, (c))
                screen.blit (words, (mx, my))
                display.flip()
                screen.blit(copy, (0, 0))
                if mb[0] == 1:
                        screen.set_clip(canvas)
                        screen.blit(words, (mx, my))
                        copy = screen.copy()
                        subc = sub.copy()       
        
        screen.set_clip()

# Polygon tool
def polygon():
        global mx, my, mb, copy, keys, pts, c, polythick, new
        if mb[0] == 1 and canvas.collidepoint(mx, my):
                new = [screen.copy()]*2 # make two copies
                
                polythick = 0
                pts = [(mx, my)]
                polygon = True
                
                while mb[0] == 1:
                        event.pump()
                        mb = mouse.get_pressed()
                while polygon:
                        screen.set_clip(canvas)
                        event.get()
                        mx, my = mouse.get_pos()
                        mb = mouse.get_pressed()
                        
                        screen.blit(new[0], (0, 0)) # blit first new copy
                        
                        draw.line(screen, (c), (pts[-1]), (mx, my))
                        if mb[0] == 1:
                                new[0] = screen.copy() # first copy keeps changing
                                pts.append((mx, my)) # add to list of points
                                while mb[0] == 1:
                                        event.pump()
                                        mb = mouse.get_pressed()
                                if pts[-1] == pts[-2]: # double click to exit
                                        polygon = False
                            
                        display.flip()

                
        if len(pts)>0:
                screen.set_clip(canvas)
                screen.blit(new[1], (0, 0)) # blit second copy(unchanged)
                draw.polygon(screen, (c), pts, polythick)
                if keys[K_UP]: # adjust thickness of polygon drawn
                        polythick+=1
                if keys[K_DOWN]:
                        polythick-=1
                if mb[1] == 1:
                        pts = []
                
        screen.set_clip()


def effect_choose_box():
        draw.rect (screen, (efcol[0]), bwbox)
        draw.rect (screen, (efcol[1]), invbox)
        draw.rect (screen, (efcol[2]), brbox)
        draw.rect (screen, (efcol[3]), darkbox)
        draw.rect (screen, (efcol[4]), funkybox)
        draw.rect (screen, (efcol[5]), negbox)
        draw.rect (screen, (efcol[6]), redbox)
        draw.rect (screen, (efcol[7]), greenbox)
        draw.rect (screen, (efcol[8]), bluebox)
        screen.blit(font.render("Black and",True, white), (150, 175))
        screen.blit(font.render("   White",True, white), (150, 195))
        screen.blit(font.render("Invert",True, white), (170, 255))
        screen.blit(font.render("Brighten",True, white), (160, 325))
        screen.blit(font.render("Darken",True, white), (160, 395))
        screen.blit(font.render("FUNKY",True, white), (220, 465))
        screen.blit(font.render("Brighten",True, white), (160, 325))
        screen.blit(font.render("Negative",True, white), (275, 185))
        screen.blit(font.render("Increase",True, white), (277, 245))
        screen.blit(font.render("Red",True, white), (290, 265))
        screen.blit(font.render("Increase",True, white), (280, 315))
        screen.blit(font.render("Green",True, white), (287, 335))
        screen.blit(font.render("Increase",True, white), (280, 385))
        screen.blit(font.render("Blue",True, white), (290, 405))


def effect_choose():
        box = Rect (120, 150, 280, 410)
        global eftype, neftype
        
        draw.rect(screen, (100, 100, 100), effectbox)
        draw.rect (screen, (green), (15, 405, 60, 60), 1)
        screen.blit(font.render("Effects",True,  purple), (20, 425))
        
        effectback.set_alpha(150)
        screen.blit(effectback, (box))
        draw.rect (screen, (black), (box), 1)
        
        
        # draw cancel an select
        draw.rect (screen, (red), efcancel)
        draw.rect (screen, (green), efselect)
        
        choosing_effect = True
        
        while choosing_effect:
                effect_choose_box()
                event.get()
                mx, my = mouse.get_pos()
                mb = mouse.get_pressed()
                for i in range(len(efcol)):
                        efcol[i] = (100, 100, 100)

                if bwbox.collidepoint(mx, my) and mb[0] == 1:
                        neftype = "b and w"
                        
                if invbox.collidepoint(mx, my) and mb[0] == 1:
                        neftype = "inverse"
                        
                if brbox.collidepoint(mx, my) and mb[0] == 1:
                        neftype = "brighten"
                        
                if darkbox.collidepoint(mx, my) and mb[0] == 1:
                        neftype = "darken"
                        
                if funkybox.collidepoint(mx, my) and mb[0] == 1:
                        neftype = "funky"
                        
                if negbox.collidepoint(mx, my) and mb[0] == 1:
                        neftype = "negative"
                        
                if redbox.collidepoint(mx, my) and mb[0] == 1:
                        neftype = "red"
                        
                if greenbox.collidepoint(mx, my) and mb[0] == 1:
                        neftype = "green"
                        
                if bluebox.collidepoint(mx, my) and mb[0] == 1:
                        neftype = "blue"
                
                # change colour of boxes if selected
                if neftype == "b and w":
                        efcol[0] = dgreen
                elif neftype == "inverse":
                        efcol[1] = dgreen
                elif neftype == "brighten":
                        efcol[2] = dgreen
                elif neftype == "darken":
                        efcol[3] = dgreen
                elif neftype == "funky":
                        efcol[4] = dgreen
                elif neftype == "negative":
                        efcol[5] = dgreen
                elif neftype == "red":
                        efcol[6] = dgreen
                elif neftype == "green":
                        efcol[7] = dgreen
                elif neftype == "blue":
                        efcol[8] = dgreen

                
                if efcancel.collidepoint(mx, my) and mb[0] == 1:
                        choosing_effect = False
                if efselect.collidepoint(mx, my) and mb[0] == 1:
                        choosing_effect = False
                        eftype = neftype # if selected, eftype will become the new eftype (neftype)
                display.flip()
        

def effect():
        global mb, mx, my, copy, subc
        if mb[0] == 1 and canvas.collidepoint(mx, my):
                
                draw.rect(screen, (100, 100, 100), effectbox)
                draw.rect (screen, (green), (15, 405, 60, 60), 1)
                screen.blit(font.render("Effects",True,  purple), (20, 425))
                
                new = screen.copy()
                effecting = True
                w = 0
                h = 0
                while effecting:
                        
                        screen.set_clip(canvas)
                        screen.blit(new, (0, 0))
                        
                        event.get()
                        nx, ny = mouse.get_pos()
                        mb = mouse.get_pressed()
                        
                        w = nx-mx 
                        h = ny-my
                        efbox = Rect(mx, my, w, h)
                        efbox.normalize()
                        draw.rect(screen, (blue), efbox, 1) # draw the rect that effect will take place in
                        display.flip()
                        
                        if mb[0] == 0:
                                effecting = False

                screen.blit(copy, (0, 0))

                if eftype == "b and w": # average out RGBs
                        for f in range (w):
                                for l in range (h):
                                        newcol = screen.get_at((f+mx, l+my))
                                        avr = (newcol[0]+newcol[1]+newcol[2])/3
                                        
                                        screen.set_at((f+mx, l+my), (avr, avr, avr))
                                        

                if eftype == "inverse": # flip position of RGB
                        for f in range (w):
                                for l in range (h):
                                        newcol = screen.get_at((f+mx, l+my))
                                        
                                        screen.set_at((f+mx, l+my), (255-newcol[0], 255-newcol[1], 255-newcol[2]))

                if eftype == "brighten": # increase RGB by 20 %
                        for f in range (w):
                                for l in range (h):
                                        newcol = screen.get_at((f+mx, l+my))
                                        newcol = [newcol[0], newcol[1], newcol[2]]
                                        newcol[0] = newcol[0]+.2*(newcol[0]) # increase 20 %
                                        newcol[1] = newcol[1]+.2*(newcol[1])
                                        newcol[2] = newcol[2]+.2*(newcol[2])
                                        if newcol[0]+.2*(newcol[0]) > 255:  # check if it goes past 255
                                                newcol[0] = 255
                                        if newcol[1]+.2*(newcol[1]) > 255:
                                                newcol[1] = 255
                                        if newcol[2]+.2*(newcol[2]) > 255:
                                                newcol[2] = 255
                                        
                                        screen.set_at((f+mx, l+my), (newcol[0], newcol[1], newcol[2]))

                if eftype == "darken": # reduce RGB by 20 %
                        for f in range (w):
                                for l in range (h):
                                        newcol = screen.get_at((f+mx, l+my))
                                        newcol = [newcol[0], newcol[1], newcol[2]]
                                        newcol[0] = newcol[0]-.2*(newcol[0]) # reduce 20 %
                                        newcol[1] = newcol[1]-.2*(newcol[1])
                                        newcol[2] = newcol[2]-.2*(newcol[2])
                                        if newcol[0]-.2*(newcol[0]) > 255: # check if it goes below 0
                                                newcol[0] = 0
                                        if newcol[1]-.2*(newcol[1]) > 255:
                                                newcol[1] = 0
                                        if newcol[2]-.2*(newcol[2]) > 255:
                                                newcol[2] = 0
                                        
                                        screen.set_at((f+mx, l+my), (newcol[0], newcol[1], newcol[2]))

                if eftype == "funky": # switch positions of RGBs
                        for f in range (w):
                                for l in range (h):
                                        newcol = screen.get_at((f+mx, l+my))
                                        
                                        screen.set_at((f+mx, l+my), (255-newcol[1], 255-newcol[2], 255-newcol[0]))

                if eftype == "negative": # same as inverse, but black and white
                        for f in range (w):
                                for l in range (h):
                                        newcol = screen.get_at((f+mx, l+my))
                                        avr = (newcol[0]+newcol[1]+newcol[2])/3
                                        screen.set_at((f+mx, l+my), (255-avr, 255-avr, 255-avr))

                if eftype == "red": # reduce green and blue values
                        for f in range (w):
                                for l in range (h):
                                        newcol = screen.get_at((f+mx, l+my))
                                        newcol = [newcol[0], newcol[1], newcol[2]]
                                        
                                        newcol[1] = newcol[1]-.2*(newcol[1])
                                        newcol[2] = newcol[2]-.2*(newcol[2])
                                        
                                        if newcol[1]-.2*(newcol[1]) > 255:
                                                newcol[1] = 0
                                        if newcol[2]-.2*(newcol[2]) > 255:
                                                newcol[2] = 0
                                        
                                        screen.set_at((f+mx, l+my), (newcol[0], newcol[1], newcol[2]))

                if eftype == "green": # reduce red and blue values
                        for f in range (w):
                                for l in range (h):
                                        newcol = screen.get_at((f+mx, l+my))
                                        newcol = [newcol[0], newcol[1], newcol[2]]
                                        newcol[0] = newcol[0]-.2*(newcol[0]) 
                                        
                                        newcol[2] = newcol[2]-.2*(newcol[2])
                                        if newcol[0]-.2*(newcol[0]) > 255: 
                                                newcol[0] = 0
                                        
                                        if newcol[2]-.2*(newcol[2]) > 255:
                                                newcol[2] = 0
                                        
                                        screen.set_at((f+mx, l+my), (newcol[0], newcol[1], newcol[2]))

                if eftype == "blue": # reduce red and green values
                        for f in range (w):
                                for l in range (h):
                                        newcol = screen.get_at((f+mx, l+my))
                                        newcol = [newcol[0], newcol[1], newcol[2]]
                                        newcol[0] = newcol[0]-.2*(newcol[0]) 
                                        newcol[1] = newcol[1]-.2*(newcol[1])
                                        
                                        if newcol[0]-.2*(newcol[0]) > 255: 
                                                newcol[0] = 0
                                        if newcol[1]-.2*(newcol[1]) > 255:
                                                newcol[1] = 0
                                        
                                        
                                        screen.set_at((f+mx, l+my), (newcol[0], newcol[1], newcol[2]))
                
                                
                screen.set_clip()
                copy = screen.copy()
        
###############################  MAIN PROGRAM  #################################


while running:
        
        for evt in event.get():
                if evt.type == QUIT:
                        running = False

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        keys = key.get_pressed()

        # clear screen if right button pressed
        if mb[2] == 1:
                clrscreen()
        
        # draw background and canvas
        background()
        screen.blit(subc, (canvas))
        
        # set colours according to sliders
        R = (Rslider-200)/2
        B = (Bslider-200)/2
        G = (Gslider-200)/2
        c = (R, G, B)

        # setting the tool information
        currentcolour = font.render ("current colour", True, (white))
        toolselected = font.render ("Tool Selected: ", True, (0,0,0))
        toolinfo = font.render(info_message,True,(0,0,0))
        toolselect = font.render(selected_message, True, (255, 0, 255))
        info_message = ""

        # draw border around canvas
        draw.rect (screen, (c), bcanvas, 3)
        draw.rect (screen, (c), toolinfobox, 3)
        
        # display tool information
        draw.rect (screen, (90, 90, 90), toolinfobox)
        screen.blit (toolinfo, (110, 580))
        screen.blit (toolselect, (230, 600))
        screen.blit (toolselected, (110, 600))
        screen.blit (currentcolour, (10, 680))

        # current colour box
        draw.rect (screen, (c), (35, 640, 35, 35))
        draw.rect (screen, (255, 255, 255), colourbox, 1)

        # drawbuttons
        drawsv()
        drawbuttons()

        # thicknesses and colours for tool boxes
        buttoncols = [blue]*10
        buttonthicks = [1] * 10
        
        # making R, B, G, sliders and moving them
        draw.line (screen, (255, 0, 0), (200, 640), (710, 640))
        draw.line (screen, (0, 0, 255), (200, 660), (710, 660))
        draw.line (screen, (0, 255, 0), (200, 680), (710, 680))
        draw.rect (screen, (255, 0, 0), (Rslider, 633, 9, 14))
        draw.rect (screen, (0, 0, 255), (Bslider, 653, 9, 14))
        draw.rect (screen, (0, 255, 0), (Gslider, 673, 9, 14))
        if Rbox.collidepoint (mx, my) and mb[0] == 1:
                Rslider = mx
        if Bbox.collidepoint (mx, my) and mb[0] == 1:
                Bslider = mx
        if Gbox.collidepoint (mx, my) and mb[0] == 1:
                Gslider = mx
        
        # copy current screen state, and redraw
        subc = sub.copy() # a copy of the canvas
        copy = screen.copy() # a copy of ovarall screen

        # select tool function
        tool_select()


        # load/save
        if savet.collidepoint(mx, my):
                info_message = "Save Tool: Save your work (use IDLE shell to enter filename)"
                if mb[0] == 1:
                        save()

        if loadt.collidepoint(mx, my):
                info_message = "Load Tool: Load previous work (use IDLE shell to enter filename)"
                if mb[0] == 1:
                        load()
                        subc = sub.copy()

        
        # run functions based on currently selected tool
        if currtool == "pencil":
                currbuttoncol[0] = 2 # change colour of button (same for the rest of tools below)
                buttoncols[0] = green
                buttonthicks[0] = 2
                pencil(mx, my, c)
                subc = sub.copy()

        elif currtool == "eraser":
                currbuttoncol[1] = 2
                buttoncols[1] = green
                buttonthicks[1] = 2

                # change size
                if keys[K_UP] == 1:
                        radiuseraser+=0.5
                if keys[K_DOWN] == 1:
                        radiuseraser-= 0.5
                        if radiuseraser < 1:
                                radiuseraser = 1
                erase(mx, my, copy, radiuseraser)
                subc = sub.copy()
                
        elif currtool == "spray":
                currbuttoncol[2] = 2
                buttoncols[2] = green
                buttonthicks[2] = 2
                moving = True
                radbox = Rect (25, 390, 10, 150)
                sizebox = Rect (65, 390, 10, 150)

                # draw the sliders on the right 
                draw.rect (screen, (100, 100, 100), (15, 350, 70, 200))
                draw.line (screen, (0, 0, 0), (30, 390), (30, 540))
                draw.line (screen, (0, 0, 0), (70, 390), (70, 540))
                draw.rect (screen, (0, 0, 0), (25, radslider, 10, 5))
                draw.rect (screen, (0, 0, 0), (65, sizeslider, 10, 5))

                
                if radbox.collidepoint(mx, my) and mb[0] == 1:
                        radslider = my
                if sizebox.collidepoint(mx, my) and mb[0] == 1:
                        sizeslider = my
   
                spray(mx, my, radslider, sizeslider, c)
                subc = sub.copy()
                
        elif currtool == "line":
                currbuttoncol[3] = 2
                buttoncols[3] = green
                buttonthicks[3] = 2
                line(mx, my, c, copy)
                subc = sub.copy()
                
        elif currtool == "paintbr":
                currbuttoncol[4] = 2
                buttoncols[4] = green
                buttonthicks[4] = 2

                # change size
                if keys[K_UP] == 1:
                        radiuspaint+=0.5
                if keys[K_DOWN] == 1:
                        radiuspaint-= 0.5
                        if radiuspaint < 1:
                                radiuspaint = 1
                paint(mx, my, radiuspaint)
                

        elif currtool == "stamp":
                currbuttoncol[5] = 2
                buttoncols[5] = green
                buttonthicks[5] = 2
                inc = 0  # how fast the stamps move
                screen.set_clip(stamps)
                if stamps.collidepoint(mx, my):
                        inc = -(my-360)/25 # stamps move according to mouse position
                        
                for i in range (num_stamps):
                        if spot[i] > 625:
                                spot[i] = spot[i-(num_stamps-1)]-57 # complicated...
                        sstamps[i].set_alpha(255) # set the to full transparency if selecting stamps
                        screen.blit (sstamps[i], (805, spot[i]))
                        srects[i] = Rect(805, spot[i], 100, 53) # the rects that the stamps are within
                        spot[i]+=inc
                        if spot[i] < 10:
                                spot[i] = spot[i-1]+57

                        # select stamp that person picks
                        if srects[i].collidepoint(mx, my):
                                draw.rect (screen, (255, 0, 255), (805, spot[i], 90, 53), 2)
                                if mb[0] == 1:
                                        current = bstamps[i]
                                        currentspot = i
                        draw.rect (screen, (0, 255, 0), (805, spot[currentspot], 90, 53), 2)
                                
                
                if canvas.collidepoint(mx, my):
                        background()
                        stamp(mx, my, current, spot)
                if canvas.collidepoint(mx, my) == False and stamps.collidepoint(mx, my) == False:
                        screen.set_clip()
                
        elif currtool == "shape":
                currbuttoncol[6] = 2
                buttoncols[6] = green
                buttonthicks[6] = 2

                # draw the boxes for circle and square tool
                draw.rect (screen, (squarecol), squarerect)
                draw.rect (screen, (circlecol), circlerect)
                draw.rect (screen, (black), (25, 380, 50, 50), 1)
                draw.ellipse (screen, (black), (25, 460, 50, 50), 1)
                squarecol = 100, 100, 100
                circlecol = 100, 100, 100
                
                if squarerect.collidepoint(mx, my):
                        info_message = "Rectangle Tool: Draw squares/rectangles"
                        if mb[0] == 1:
                                shapetool = "square"
                                
                if circlerect.collidepoint(mx, my):
                        info_message = "Circle Tool: Draw ovals/circles"
                        if mb[0] == 1:
                                shapetool = "circle"
                                

                if shapetool == "square":
                        squarecol = 0, 255, 0
                        square(mx, my, c, copy)
                        selected_message = "Rectangle: adjust thickness with up/down arrow keys while drawing"
                
                        
                if shapetool == "circle":
                        circlecol = 0, 255, 0
                        circle(mx, my, c, copy)
                        selected_message = "Circle: adjust thickness with up/down arrow keys while drawing"
                subc = sub.copy()
                
        elif currtool == "effect":
                currbuttoncol[7] = 2
                buttoncols[7] = green
                buttonthicks[7] = 2
                
                effect()
                
                # go to selecting effect type
                if effectbox.collidepoint (mx, my) and mb[0] ==1:
                        effect_choose()
                        screen.blit(copy, (0, 0))
                draw.rect(screen, (100, 100, 100), effectbox)
                draw.rect (screen, (green), (15, 405, 60, 60), 1)
                screen.blit(font.render("Effects",True,  purple), (20, 425))
                
                subc = sub.copy()

                
        elif currtool == "eyedropper":
                currbuttoncol[8] = 2
                buttoncols[8] = green
                buttonthicks[8] = 2

                # get RGB of the spot selected
                if mb[0] == 1 and canvas.collidepoint(mx, my):      
                        c = screen.get_at ((mx, my))
                        Rslider = c[0]*2+200
                        Bslider = c[2]*2+200
                        Gslider = c[1]*2+200

        elif currtool == "polygon":
                currbuttoncol[9] = 2
                buttoncols[9] = green
                buttonthicks[9] = 2

               
                if canvas.collidepoint(mx, my):
                        polygon()
                        
                        subc = sub.copy()

        
                        
        
        # colour palette
        if colourbox.collidepoint(mx, my):
                info_message = "Click to open colour palette (can also be opened using middle mouse button)"

        if (mb [1] == 1) or (colourbox.collidepoint(mx, my) and mb[0] == 1):
                col_choose()

        display.flip()  # one for the entire whole program
        
        screen.blit(copy, (0, 0))

# do i really need a comment for this part =P
quit()

# CREDITS
# idea of using arrow keys to adjust sizes given by someone else
# idea of using jpeg image for colour palette given by other person
# idea of using effects given by someone else

# all methods/code used are copyrighted (is that even a word =S)
# Saad Ahmed inc., 2009
# any acts of ingringement will result in excecution by law and/or worser punishment
