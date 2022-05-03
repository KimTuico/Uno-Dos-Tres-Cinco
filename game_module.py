import pyglet
from random import randint
from pyglet.window import key
from pyglet.window import mouse
from home_screen_module import location_update
from home_screen_module import get_nickname
from menu_module import update_file

pyglet.resource.path = ["resources"]
pyglet.resource.reindex()

# Background Picture
bgpicture = pyglet.resource.image('bg_game.jpg')
bgSprite = pyglet.sprite.Sprite(bgpicture)
bgSprite.scale = 0.713
bgSprite.position = (0,0)

# Return Box
ret = pyglet.resource.image('hsreturn.jpg')
retSprite = pyglet.sprite.Sprite(ret)
retSprite.scale = 0.7
retSprite.position = (1024-retSprite.width , 768-retSprite.height )

scorelabel = pyglet.text.Label('Grades', font_size=12, x = 20, y = 20)

# Creates Oble
playerImage = pyglet.resource.image("oble.png")
player = pyglet.sprite.Sprite(playerImage)
player.scale = .5
player.position = (0,50)

# Creates Grade
grades_seq =[pyglet.resource.image("1.png"), pyglet.resource.image("2.png"), pyglet.resource.image("3.png"), pyglet.resource.image("4.png"),
            pyglet.resource.image("5.png"), pyglet.resource.image("6.png"), pyglet.resource.image("7.png"), pyglet.resource.image("8.png"),
            pyglet.resource.image("9.png"), pyglet.resource.image("10.png"),
            pyglet.resource.image("11.png"), pyglet.resource.image("12.png"), pyglet.resource.image("13.png"), pyglet.resource.image("14.png"),
            pyglet.resource.image("15.png"), pyglet.resource.image("16.png"), pyglet.resource.image("17.png"), pyglet.resource.image("18.png"),
            pyglet.resource.image("19.png"),] 
falling = []
plunk = pyglet.resource.media('receive.wav', streaming=False)

def game_mouse_motion(x, y, dx, dy):
    player.x, player.y = x-playerImage.width/4, 50

def game_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT and x >= 1024-retSprite.width and x <= 1024 and y >= 768-retSprite.height and y <= 768:
            reset_game()
            location_update(0)

def game_draw(window):
    window.clear()
    bgSprite.draw()
    scorelabel.draw()
    retSprite.draw()
    for f in falling:
        x = pyglet.sprite.Sprite(grades_seq[f[0]])
        x.position = (f[1], f[2])
        x.draw()
    player.draw()
    

ticks = 0
score = 0
prev_score = 0

def reset_game():
    global ticks
    global score
    global prev_score
    ticks = 0
    prev_score = score
    score = 0
    falling.clear()
    player.position = (0,50)

scoring = [90,80,75,70,45,40,35,30,10,0,0,0,0,0,0,0,0,0,0]

def difficulty(s):
    if s>50000:
        x = randint(0,9)
        return 0 if x==0 else randint(9,18)
    elif s>25000:
        return randint(0,18)
    else:
        return randint(0,9)


def updates(dt,bgm):
    global ticks, falling, score, scorelabel, plunk
    ticks += 1
    for f in falling:
        # Check for a catch. Player must be close to the Grade
        if 50 <= f[2] <= 200 and player.x - 60 <= f[1] <= player.x + 60: 
            if f[0] >= 9:
                update_file(get_nickname(),str(score))
                reset_game()
                location_update(5)
            f[2] = 0
            score = score + scoring[f[0]]
            if not bgm.mute_state():
                plunk.play()
            scorelabel.text = "Grade: %06d" % score
        speed = f[0] if f[0] < 9 else randint(0,8)
        f[2] = f[2] - 2*(3-speed/3+1) - int(score/2000)
    
    # removes grades that are caught or beyond the screen
    falling_new = [f for f in falling if f[2] > 0]
    
    
    # adds new grade
    if len(falling_new) <= 10 and ticks % 20 == 0:
        falling_new.append([difficulty(score), randint(0,900), 800])
    falling = falling_new
    
    
# TRY AGAIN FUNCTIONS
# Grayish Background
coverSprite = pyglet.sprite.Sprite(pyglet.resource.image('cover.jpg'))
coverSprite.scale_x = 3
coverSprite.scale_y = 3
coverSprite.position = (0,0)

# Dialog Box
description = pyglet.resource.image('retry.png')
dboxSprite = pyglet.sprite.Sprite(description)
dboxSprite.scale = 0.7
dboxSprite.position = ((1024-dboxSprite.width)/2 , (768-dboxSprite.height)/2 - 10 )

# Try Again 
try_again = pyglet.resource.image('try.png')
trySprite = pyglet.sprite.Sprite(try_again)
trySprite.scale = 0.7
trySprite.position = (0,-200)

# Try Again 
return_menu = pyglet.resource.image('return.png')
retmenSprite = pyglet.sprite.Sprite(return_menu)
retmenSprite.scale = 0.7
retmenSprite.position = (0,-200)

# Score
scoreText = pyglet.text.Label(str(prev_score), font_size = 28, x = 1024/2, y = 370, anchor_x = 'center', anchor_y = 'center', bold = True)

def try_again_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT and x >= 528  and x <= 775 and y >= 278 and y <= 321:
        location_update(0)
    elif button == mouse.LEFT and x >= 248 and x <= 495 and y >= 278 and y <= 321:
        location_update(4)

def try_again_mouse_motion(x, y, button, modifiers):
    if x >= 528  and x <= 775 and y >= 278 and y <= 321:
        retmenSprite.position = (528, 257.5)
    elif x >= 248 and x <= 495 and y >= 278 and y <= 321:
        trySprite.position = (248.5, 257.5)
    else:
        retmenSprite.position = (0,-200)
        trySprite.position = (0, -200)

def try_again_draw(window):
    window.clear()
    bgSprite.draw()
    coverSprite.draw()
    dboxSprite.draw()
    scoreText.text = str(prev_score)
    scoreText.draw()
    trySprite.draw()
    retmenSprite.draw()