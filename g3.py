import pgzrun

WIDTH = 700
HEIGHT = 500



#actor
p = Actor('char1',(50,200))            #(50,200) -> position
#speed = 7                            #speed decleration

def draw():
    screen.fill('white')
    p.draw()

def update():
    player_controls()

def player_controls():
    if (keyboard.UP and not p.top < 0):
        p.y += -6
        p.angle = 0
    elif keyboard.DOWN and not p.bottom > HEIGHT:
        p.y += 6
        p.angle = 180
    elif keyboard.LEFT and not p.left < 0:
        p.x += -6
        p.angle = 90
    elif keyboard.RIGHT and not p.right > WIDTH:
        p.x += 6
        p.angle = -90
    else:
        p.angle = 0

    
    

pgzrun.go()