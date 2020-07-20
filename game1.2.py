from pygame_functions2 import *

screenSize(1024,768)
setBackgroundColour('green')
setAutoUpdate(False)
link = makeSprite("LinkSimple.png", 14)
octorok = makeSprite("Octorok.png", 4, 2)
showSprite(link)
showSprite(octorok)
Link_X = 500
Link_Y = 350
moveSprite(link, Link_X, Link_Y)
moveSprite(octorok, 200, 200)
LINK_SPEED = 4

nextFrame = clock()
frame = 0
orientation = 0

while True:
    if clock() >nextFrame:
        frame= (frame + 1)%2
        nextFrame += 80
        pause(10)
        
        if keyPressed("down"):
            changeSpriteImage(link, 0*2 + frame)
            orientation =0
            Link_Y = Link_Y + LINK_SPEED
        if keyPressed("up"):
            changeSpriteImage(link, 1*2 + frame)
            orientation =1
            Link_Y = Link_Y - LINK_SPEED
        if keyPressed("right"):
            changeSpriteImage(link, 2*2 + frame)
            orientation =2
            Link_X = Link_X + LINK_SPEED
        if keyPressed("left"):
            changeSpriteImage(link, 3*2 + frame)
            orientation =3
            Link_X = Link_X - LINK_SPEED
        if keyPressed("space"):
            changeSpriteImage(link, orientation + 8)
        if keyPressed("h"):
            changeSpriteImage(link, frame+12)
        
        moveSprite(link, Link_X, Link_Y)
        updateDisplay()

endWait()