from tkinter import *
from tkinter import filedialog
from pygame import *
from random import *

root = Tk()
root.withdraw()

screen = display.set_mode((1000,600))

# Transparency Setup
# Highlight
cover = Surface((100,100)).convert()                  # make blank Surface
cover.set_alpha(5)
cover.fill((255,0,255)) 
cover.set_colorkey((255,0,255))
draw.circle(cover,(255,255,0),(50,50),10)
# Glow
cover2 = Surface((100,100)).convert()                  # make blank Surface
cover2.set_alpha(5)
cover2.fill((255,0,255)) 
cover2.set_colorkey((255,0,255))
draw.circle(cover2,(255,255,0),(50,50),11)

# Background
background = image.load("Images/background.png")
background = transform.smoothscale(background,(1000,600))
screen.blit(background,(0,0))
hide = screen.subsurface(750,505,240,40).copy()

# Canvas
canvasRect = Rect(115,80,600,470)
draw.rect(screen,(255,255,255), canvasRect)
blank = screen.subsurface(canvasRect).copy()    # placeholder in undo list

# Variables
mx,my = 0,0
c = 0
c2 = (255,255,0)
size = 10
undolist = [blank]
redolist = []
result = ""
glow = False
points = []

# Text
font.init()
comicFont = font.SysFont("Helvetica",28)
titleFont = font.SysFont("CooperBlack", 40)
infoFont = font.SysFont("Calibri",16)

# Images
pencilPic = image.load("Images/pencil.png")
eraserPic = image.load("Images/eraser.png")
markerPic = image.load("Images/marker.png")
fillPic = image.load("Images/fill.png")
eyedropPic = image.load("Images/eyedropper.png")
sprayPic = image.load("Images/spray.png")
highlightPic = image.load("Images/highlight.png")
glowPic = image.load("Images/glow.png")

ovalPic = image.load("Images/oval.png")
unfillovalPic = image.load("Images/unfilloval.png")
rectPic = image.load("Images/rect.png")
unfillrectPic = image.load("Images/unfillrect.png")
linePic = image.load("Images/line.png")

coconutPic = image.load("Images/coconut.png")
sunglassPic = image.load("Images/sunglass.png")
palmtreePic = image.load("Images/palmtree.png")
beachballPic = image.load("Images/beachball.png")
shellPic = image.load("Images/shell.png")
crabPic = image.load("Images/crab.png")

clearPic = image.load("Images/clear.png")
savePic = image.load("Images/save.png")
openPic = image.load("Images/open.png")
undoPic = image.load("Images/undo.png")
redoPic = image.load("Images/redo.png")

colorwheelPic = image.load("Images/colorpalette.png")
screen.blit(colorwheelPic,(750,80))
colorRect = Rect(750,80,225,225)

# Tools
pencilRect = Rect(30,60,50,50)
eraserRect = Rect(30,115,50,50)
markerRect = Rect(30,170,50,50)
sprayRect = Rect(30,225,50,50)
eyedropRect = Rect(30,280,50,50)
fillRect = Rect(30,335,50,50)
highlightRect = Rect(30,390,50,50)
glowRect = Rect(30,445,50,50)
# Shapes
ovalRect = Rect(750,315,50,50)
unfillovalRect = Rect(810,315,50,50)
rectRect = Rect(750,375,50,50)
unfillrectRect = Rect(810,375,50,50)
lineRect = Rect(750,435,110,50)
# Stamps
coconutRect = Rect(870,315,50,50)
sunglassRect = Rect(930,315,50,50)
palmtreeRect = Rect(870,375,50,50)
beachballRect = Rect(930,375,50,50)
shellRect = Rect(870,435,50,50)
crabRect = Rect(930,435,50,50)
# Save/Open/Clear/Undo/Redo
openRect = Rect(115,35,40,40)
saveRect = Rect(160,35,40,40)
clearRect = Rect(675,35,40,41)
undoRect = Rect(15,510,40,40)
redoRect = Rect(60,510,40,40)

# Pasting images
screen.blit(pencilPic,(pencilRect))
screen.blit(eraserPic,(eraserRect))
screen.blit(fillPic,(fillRect))
screen.blit(eyedropPic,(eyedropRect))
screen.blit(markerPic,(markerRect))
screen.blit(sprayPic,(sprayRect))
screen.blit(highlightPic,(highlightRect))
screen.blit(glowPic,(glowRect))

screen.blit(ovalPic,(ovalRect))
screen.blit(unfillovalPic,(unfillovalRect))
screen.blit(rectPic,(rectRect))
screen.blit(unfillrectPic,(unfillrectRect))
screen.blit(linePic,(lineRect))

screen.blit(clearPic,(clearRect))
screen.blit(savePic,(saveRect))
screen.blit(openPic,(openRect))
screen.blit(undoPic,(undoRect))
screen.blit(redoPic,(redoRect))

# Stamp icons
# Background for stamp buttons since stamp image have transparent background
draw.rect(screen,(255,255,255),coconutRect)
draw.rect(screen,(255,255,255),sunglassRect)
draw.rect(screen,(255,255,255),palmtreeRect)
draw.rect(screen,(255,255,255),beachballRect)
draw.rect(screen,(255,255,255),shellRect)
draw.rect(screen,(255,255,255),crabRect)
# Resize for stamp icons
resizecoconut = transform.smoothscale(coconutPic,(50,50))
screen.blit(resizecoconut,(coconutRect))
resizesunglass = transform.smoothscale(sunglassPic,(50,50))
screen.blit(resizesunglass,(sunglassRect))
resizepalmtree = transform.smoothscale(palmtreePic,(50,50))
screen.blit(resizepalmtree,(palmtreeRect))
resizebeachball = transform.smoothscale(beachballPic,(50,50))
screen.blit(resizebeachball,(beachballRect))
resizeshell = transform.smoothscale(shellPic,(50,50))
screen.blit(resizeshell,(shellRect))
resizecrab = transform.smoothscale(crabPic,(50,50))
screen.blit(resizecrab,(crabRect))


tool = "pencil"

running = True
while running:
    click = False
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1:
                click = True
                start = evt.pos
                x1, y1 = start  # To get inital pos for shapes
                                # Used to find width and height
                back = screen.subsurface(canvasRect).copy()
            if evt.button == 3:
                sav = screen.subsurface(canvasRect)
                if result == "":
                    result = filedialog.asksaveasfilename(defaultextension=".png")  # saves a drawing if it hasn't been saved as a file
                    if result != "":
                        drawing = screen.subsurface(canvasRect)
                        image.save_extended(drawing,result) # Saves as a file
                else:
                    display.set_caption("Saving...")
                    image.save(sav, str(result))
                    time.delay(1000)
                    display.set_caption("Saved")
                    time.delay(500)
                display.set_caption(str(result))
            if evt.button == 4: # UP
                size += 1
                if size > 40:
                    size = 40
            if evt.button == 5: # DOWN
                size -= 1
                if size <= 0:
                    size = 0
        if evt.type == MOUSEBUTTONUP:
            if evt.button == 1:
                if canvasRect.collidepoint(start):
                    copy = screen.subsurface(canvasRect).copy()
                    undolist.append(copy)
                    redolist = []

    mb = mouse.get_pressed()            
    omx,omy = mx,my
    mx, my = mouse.get_pos()

    # Buttons
    draw.rect(screen,(0,255,0),pencilRect,2)
    draw.rect(screen,(0,255,0),eraserRect,2)
    draw.rect(screen,(0,255,0),markerRect,2)
    draw.rect(screen,(0,255,0),sprayRect,2)    
    draw.rect(screen,(0,255,0),fillRect,2)
    draw.rect(screen,(0,255,0),eyedropRect,2)
    draw.rect(screen,(0,255,0),highlightRect,2)
    draw.rect(screen,(0,255,0),glowRect,2)

    draw.rect(screen,(0,255,0),ovalRect,2)
    draw.rect(screen,(0,255,0),unfillovalRect,2)
    draw.rect(screen,(0,255,0),rectRect,2)
    draw.rect(screen,(0,255,0),unfillrectRect,2)
    draw.rect(screen,(0,255,0),lineRect,2)

    draw.rect(screen,(0,255,0),coconutRect,2)
    draw.rect(screen,(0,255,0),sunglassRect,2)
    draw.rect(screen,(0,255,0),palmtreeRect,2)
    draw.rect(screen,(0,255,0),beachballRect,2)
    draw.rect(screen,(0,255,0),shellRect,2)
    draw.rect(screen,(0,255,0),crabRect,2)

    draw.rect(screen,(0,255,0),openRect,1)
    draw.rect(screen,(0,255,0),saveRect,1)
    draw.rect(screen,(0,255,0),clearRect,1)
    draw.rect(screen,(0,255,0),undoRect,1)
    draw.rect(screen,(0,255,0),redoRect,1)

    # Text boxes
    draw.rect(screen,(255,255,255),(735,25,250,40))
    txtPic = comicFont.render(f"Current Tool: {tool.capitalize()}", True, (255,0,0))
    screen.blit(txtPic,(740,26))

    draw.rect(screen,(255,255,255),(800,550,120,40))
    txtPic = comicFont.render(f"Size: {size} px", True, (255,0,0))
    screen.blit(txtPic,(803,553))

    draw.rect(screen,(255,255,255),(235,30,370,40))
    txtPic = titleFont.render("Painter's Paradise", True, (255,0,0))
    screen.blit(txtPic,(240,27))
    # Glow FX Text Box
    if glow == True:
        draw.rect(screen,(255,255,255),(750,505,170,40))
        txtPic = infoFont.render("Press Scroll Wheel to", True, (255,0,0))
        screen.blit(txtPic,(753,508))    
        txtPic = infoFont.render("change glow color", True, (255,0,0))
        screen.blit(txtPic,(753,525))
    else:
        screen.blit(hide,(750,505,240,40))          # hide displays for glow

    # Select Color
    if colorRect.collidepoint(mx,my) and mb[0]==1:
        c = screen.get_at((mx,my))                  # Tools
        draw.circle(cover,(c),(50,50),size)         # Highlight
    if colorRect.collidepoint(mx,my) and mb[1]==1:  # For Glow
        c2 = screen.get_at((mx,my))
        draw.circle(cover2,(c2),(50,50),(size+1))       

    # Tranparency Color
    if glow == True:
        cover2.fill((255,0,255))
        draw.circle(cover2,(c2),(50,50),(size+1))
    if tool == "highlight":
        cover.fill((255,0,255))
        draw.circle(cover,(c),(50,50),(size))

    # Current Color Display
    draw.rect(screen,c,(950,550,40,40))         # Drawing color
    draw.rect(screen,(0),(950,550,40,40),2)     # outline
    if glow == True:
        draw.rect(screen,c2,(950,505,40,40))    # Glow color
        draw.rect(screen,(0),(950,505,40,40),2) # outline        
    # ----------------------------------
    # Select tool
    if click:
        if pencilRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,0),pencilRect,2)
            tool = "pencil"
        if eraserRect.collidepoint(mx,my):
            glow = False
            screen.blit(glowPic,(glowRect))
            draw.rect(screen,(255,255,0),eraserRect,2)
            tool = "eraser"
        if markerRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,0),markerRect,2)
            tool = "marker"
        if sprayRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,0),sprayRect,2)
            tool = "spray"      
        if eyedropRect.collidepoint(mx,my):
            glow = False
            screen.blit(glowPic,(glowRect))
            draw.rect(screen,(255,255,0),eyedropRect,2)
            tool = "eyedrop"
        if fillRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,0),fillRect,2)
            tool = "fill"
        if highlightRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,0),highlightRect,2)
            tool = "highlight"
        if glowRect.collidepoint(mx,my):
            if glow == True:
                glow = False
                screen.blit(glowPic,(glowRect))
            else:
                glow = True
                draw.rect(screen,(255,255,0),glowRect)

        if ovalRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,0),ovalRect,2)
            tool = "oval"
        if unfillovalRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,0),unfillovalRect,2)
            tool = "unfill oval"
        if rectRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,0),rectRect,2)
            tool = "rect"
        if unfillrectRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,0),unfillrectRect,2)
            tool = "unfill rect"
        if lineRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,0),lineRect,2)
            tool = "line"

        if coconutRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,0),coconutRect,2)
            tool = "coconut"
        if sunglassRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,0),sunglassRect,2)
            tool = "sunglass"
        if palmtreeRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,0),palmtreeRect,2)
            tool = "palmtree"
        if beachballRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,0),beachballRect,2)
            tool = "beachball"
        if shellRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,0),shellRect,2)
            tool = "shell"
        if crabRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,0),crabRect,2)
            tool = "crab"

    # Drawing on Canvas
    if mb[0]==1 and canvasRect.collidepoint(mx,my) or canvasRect.collidepoint(omx,omy):
        screen.set_clip(canvasRect)
        if click:
             if tool == "fill":
                points = [(mx,my)]
                ocol = screen.get_at((mx,my))
                while points != []:
                    x,y = points.pop()
                    screen.get_at((x,y))
                    if (x,y) != ocol:
                        screen.set_at((x,y),c)
                        if screen.get_at((x-1,y)) == ocol:  # Checks pixel to the left
                            points.append((x-1,y))
                        if screen.get_at((x+1,y)) == ocol:  # Checks pixel to the right
                            points.append((x+1,y))
                        if screen.get_at((x,y-1)) == ocol:  # Checks pixel above
                            points.append((x,y-1))
                        if screen.get_at((x,y+1)) == ocol:  # Checks pixel below
                            points.append((x,y+1))           
        if mb[0]:
            if tool == "pencil":
                draw.line(screen,c,(omx,omy),(mx,my),2)
            if tool == "eraser":
                draw.circle(screen,(255,255,255),(mx,my),size)
            if tool == "marker":
                d = ((mx-omx)**2+(my-omy)**2)**0.5
                if d == 0:
                    d = 1
                sx = (mx - omx) / d
                sy = (my - omy) / d
                for i in range(int(d)):
                    draw.circle(screen,c,(omx+i*sx,omy+i*sy),size)
            if tool == "spray":
                x = randint(mx-size,mx+size)
                y = randint(my-size,my+size)
                r = ((x-mx)**2 + (y-my)**2)**0.5
                if r <= size:
                    draw.circle(screen,c,(x,y),1)
            if tool == "eyedrop":
                c = screen.get_at((mx,my))
                tool = "pencil"
            if tool == "highlight":
                d = ((mx-omx)**2+(my-omy)**2)**0.5
                if d == 0:
                    d = 1
                sx = (mx - omx) / d
                sy = (my - omy) / d
                for i in range(int(d)):
                    screen.blit(cover,(omx-50+i*sx,omy-50+i*sy))
            if glow == True:
                screen.blit(cover2,(mx-50,my-50))    # Disclaimer: Functions differently between v3.12 and v3.8

            if tool == "oval":
                screen.blit(back, canvasRect)
                width = mx - x1
                height = my - y1
                rec = Rect(x1,y1,width,height)
                rec.normalize()                    
                draw.ellipse(screen,c, rec)
            if tool == "unfill oval":
                screen.blit(back, canvasRect)
                width = mx - x1
                height = my - y1
                rec = Rect(x1,y1,width,height)
                rec.normalize()                    
                draw.ellipse(screen,c, rec,2)
            if tool == "rect":
                screen.blit(back, canvasRect)
                width = mx - x1
                height = my - y1
                rec = Rect(x1,y1,width,height)
                rec.normalize()
                draw.rect(screen,c, rec)
            if tool == "unfill rect":
                screen.blit(back, canvasRect)
                width = mx - x1
                height = my - y1
                rec = Rect(x1,y1,width,height)
                rec.normalize()                    
                draw.rect(screen,c, rec,2)
            if tool == "line":
                screen.blit(back, canvasRect)
                draw.line(screen, c, start,(mx,my), size)

            if tool == "coconut":
                screen.blit(back,canvasRect)
                x = mx - (coconutPic.get_width()/2)     # center x
                y = my - (coconutPic.get_height()/2)    # center y
                screen.blit(coconutPic, (x,y))
            if tool == "sunglass":
                screen.blit(back,canvasRect)               
                x = mx - (sunglassPic.get_width()/2)
                y = my - (sunglassPic.get_height()/2)
                screen.blit(sunglassPic, (x,y))
            if tool == "palmtree":
                screen.blit(back,canvasRect)                 
                x = mx - (palmtreePic.get_width()/2)
                y = my - (palmtreePic.get_height()/2)                   
                screen.blit(palmtreePic, (x,y))
            if tool == "beachball":
                screen.blit(back,canvasRect)
                x = mx - (beachballPic.get_width()/2)
                y = my - (beachballPic.get_height()/2)                 
                screen.blit(beachballPic, (x,y))
            if tool == "shell":
                screen.blit(back,canvasRect)
                x = mx - (shellPic.get_width()/2)
                y = my - (shellPic.get_height()/2)                 
                screen.blit(shellPic, (x,y))
            if tool == "crab":
                screen.blit(back,canvasRect)
                x = mx - (crabPic.get_width()/2)
                y = my - (crabPic.get_height()/2)                 
                screen.blit(crabPic, (x,y))

        screen.set_clip(None)
        display.set_caption("Right click to save canvas to file")

    # Save|Open|Clear|Undo|Redo 
    if click:
        if openRect.collidepoint(mx,my):
            result = filedialog.askopenfilename(filetypes = [("Picture files", "*.png;*.jpg")])
            print(result)
            if result != "":    # Crash-preventer if "Cancel" is selected
                pic = image.load(result)
                if pic.get_size() != (600,470):  # resize if user uploads picture bigger than canvas size
                    pic = transform.smoothscale(pic,(600,470))
                    screen.blit(pic,canvasRect)
                else:
                    screen.blit(pic,canvasRect)
        elif saveRect.collidepoint(mx,my):
            result = filedialog.asksaveasfilename(defaultextension=".png",filetypes = [("Picture files", "*.png;*.jpg")])   # defaultextension adds .png to file if no extension is added
            print(result)
            if result != "":    # Crash-preventer if "Cancel" is selected
                drawing = screen.subsurface(canvasRect)
                image.save_extended(drawing,result)
                display.set_caption(str(result))
        elif clearRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,255),canvasRect)
        elif undoRect.collidepoint(mx, my):
            if len(undolist) != 1: # Crash-preventer
                redolist.append(undolist[-1])
                undolist = undolist[:-1]
                undo = undolist[-1]
                screen.blit(undo, canvasRect)
        elif redoRect.collidepoint(mx, my):
            if redolist != []: # Crash-preventer
                redo = redolist[-1]
                screen.blit(redo, canvasRect)
                undolist.append(redo)
                redolist = redolist[:-1]
    # ----------------------------------
    display.flip()

quit()
