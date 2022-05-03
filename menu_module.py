import pyglet
from pyglet.window import key
from pyglet.window import mouse
from home_screen_module import location_update
from home_screen_module import nickname_update

pyglet.resource.path = ["resources"]
pyglet.resource.reindex()



# DESCRIPTION FUNCTIONS
# Background Picture 2
bg2picture = pyglet.resource.image('bg_game.jpg')
bg2Sprite = pyglet.sprite.Sprite(bg2picture)
bg2Sprite.scale =  0.713
bg2Sprite.position = (0,0)

# Grayish Background
coverSprite = pyglet.sprite.Sprite(pyglet.resource.image('cover.jpg'))
coverSprite.scale_x = 3
coverSprite.scale_y = 3
coverSprite.position = (0,0)

# Dialog Box
description = pyglet.resource.image('descontent.jpg')
dboxSprite = pyglet.sprite.Sprite(description)
dboxSprite.scale = 0.7
dboxSprite.position = ((1024-dboxSprite.width)/2 , (768-dboxSprite.height)/2 - 10 )

def description_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT and x >= 899 and x <= 963 and y >= 578 and y <= 635:
            location_update(0)

def description_draw(window):
    window.clear()
    bg2Sprite.draw()
    coverSprite.draw()
    dboxSprite.draw()
    


# HIGHSCORE FUNCTIONS
# Return Box
ret = pyglet.resource.image('hsreturn.jpg')
retSprite = pyglet.sprite.Sprite(ret)
retSprite.scale = 0.7
retSprite.position = (1024-retSprite.width , 768-retSprite.height )

# Background Picture 2
bg3picture = pyglet.resource.image('bg_highscores.jpg')
bg3Sprite = pyglet.sprite.Sprite(bg3picture)
bg3Sprite.scale =  0.713
bg3Sprite.position = (0,0)

def update_text():
    hsfile = open("highscores.txt","r")
    lines = hsfile.readlines()
    lines = lines[0].split(",")
    hsfile.close()
    
    scl = pyglet.text.Label(lines[0], font_name = 'Cenutry Gothic', font_size = 18, 
      x = 520, y = 530 , anchor_x = 'center', anchor_y = 'center', bold = True, color = (255,255,255,255))
    scls = pyglet.text.Label(lines[1], font_name = 'Cenutry Gothic', font_size = 36, 
      x = 520, y = 435, anchor_x = 'center', anchor_y = 'center', bold = True, color = (0,0,0,255))
    scl.draw()
    scls.draw()
    
    mcl = pyglet.text.Label(lines[2].replace("\n", ""), font_name = 'Cenutry Gothic', font_size = 14, 
      x = 727, y = 415 , anchor_x = 'center', anchor_y = 'center', bold = True, color = (255,255,255,255))
    mcls = pyglet.text.Label(lines[3].replace("\n", ""), font_name = 'Cenutry Gothic', font_size = 34, 
      x = 727, y = 340, anchor_x = 'center', anchor_y = 'center', bold = True, color = (0,0,0,255))
    mcl.draw()
    mcls.draw()
    
    cl = pyglet.text.Label(lines[4].replace("\n", ""), font_name = 'Cenutry Gothic', font_size = 11, 
      x = 325, y = 372 , anchor_x = 'center', anchor_y = 'center', bold = True, color = (255,255,255,255))
    cls = pyglet.text.Label(lines[5].replace("\n", ""), font_name = 'Cenutry Gothic', font_size = 32, 
      x = 325, y = 305, anchor_x = 'center', anchor_y = 'center', bold = True, color = (0,0,0,255))
    cl.draw()
    cls.draw()

def update_file(name, score):
    hsfile = open("highscores.txt","r")
    lines = hsfile.readlines()
    lines = lines[0].split(",")
    hsfile.close()
    for i in range(3):
        temp_score = score
        temp_name = name
        if int(score) > int(lines[i*2+1]):
            score = lines[i*2+1]
            name = lines[i*2]
            lines[i*2+1] = temp_score
            lines[i*2] = temp_name
    
    hsfile = open("highscores.txt","w")
    hsfile.write(','.join(lines))
    hsfile.close()

def highscore_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT and x >= 1024-retSprite.width and x <= 1024 and y >= 768-retSprite.height and y <= 768:
            location_update(0)

def highscore_draw(window):
    window.clear()
    bg3Sprite.draw()
    retSprite.draw()
    update_text()



# NICKNAME FUNCTIONS
# Background Picture 1
bg1picture = pyglet.resource.image('bg_main_menu.jpg')
bg1Sprite = pyglet.sprite.Sprite(bg1picture)
bg1Sprite.scale =  0.713
bg1Sprite.position = (0,0)

# Nickname Box
nickname = pyglet.resource.image('nickname.jpg')
boxSprite = pyglet.sprite.Sprite(nickname)
boxSprite.scale = 0.7
boxSprite.position = ((1024-boxSprite.width)/2 , (768-boxSprite.height)/2 - 10 )

# Players Name
nickname_file = open("nickname.txt","r")
nameText = pyglet.text.Label(nickname_file.read()[:len(nickname_file.read())-1], font_name = 'Cenutry Gothic', font_size = 22, 
    x = 1024/2, y = 290, anchor_x = 'center', anchor_y = 'center', bold = True)
nickname_file.close()

def nickname_key_press(symbol, modifiers):
    if symbol == key.BACKSPACE:
        nameText.text = nameText.text[:len(nameText.text)-1]
    elif symbol == key.ENTER:
        nickname_update(nameText.text+'!')
        location_update(0)
    elif len(nameText.text) <= 13:
        if symbol == key.A:
            nameText.text = nameText.text + 'A'
        elif symbol == key.B:
            nameText.text = nameText.text + 'B'
        elif symbol == key.C:
            nameText.text = nameText.text + 'C'
        elif symbol == key.D:
            nameText.text = nameText.text + 'D'
        elif symbol == key.E:
            nameText.text = nameText.text + 'E'
        elif symbol == key.F:
            nameText.text = nameText.text + 'F'
        elif symbol == key.G:
            nameText.text = nameText.text + 'G'
        elif symbol == key.H:
            nameText.text = nameText.text + 'H'
        elif symbol == key.I:
            nameText.text = nameText.text + 'I'
        elif symbol == key.J:
            nameText.text = nameText.text + 'J'
        elif symbol == key.K:
            nameText.text = nameText.text + 'K'
        elif symbol == key.L:
            nameText.text = nameText.text + 'L'
        elif symbol == key.M:
            nameText.text = nameText.text + 'M'
        elif symbol == key.N:
            nameText.text = nameText.text + 'N'
        elif symbol == key.O:
            nameText.text = nameText.text + 'O'
        elif symbol == key.P:
            nameText.text = nameText.text + 'P'
        elif symbol == key.Q:
            nameText.text = nameText.text + 'Q'
        elif symbol == key.R:
            nameText.text = nameText.text + 'R'
        elif symbol == key.S:
            nameText.text = nameText.text + 'S'
        elif symbol == key.T:
            nameText.text = nameText.text + 'T'
        elif symbol == key.U:
            nameText.text = nameText.text + 'U'
        elif symbol == key.V:
            nameText.text = nameText.text + 'V'
        elif symbol == key.W:
            nameText.text = nameText.text + 'W'
        elif symbol == key.X:
            nameText.text = nameText.text + 'X'
        elif symbol == key.Y:
            nameText.text = nameText.text + 'Y'
        elif symbol == key.Z:
            nameText.text = nameText.text + 'Z'
        elif symbol == key.SPACE:
            nameText.text = nameText.text + ' '

def nickname_draw(window):
    window.clear()
    bg1Sprite.draw()
    coverSprite.draw()
    boxSprite.draw()
    nameText.draw()
    