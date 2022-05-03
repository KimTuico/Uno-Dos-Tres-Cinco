import pyglet
from pyglet.window import key
from pyglet.window import mouse

pyglet.resource.path = ["resources"]
pyglet.resource.reindex()

# Background Picture
bgpicture = pyglet.resource.image('bg_main_menu.jpg')
bgSprite = pyglet.sprite.Sprite(bgpicture)
bgSprite.scale = 0.713
bgSprite.position = (0,0)

# New Game 
newgame = pyglet.resource.image('newgame.jpg')
newSprite = pyglet.sprite.Sprite(newgame)
newSprite.scale = 0.7178
newSprite.position = (0,-200)
newLeft, newBottom = 656,318.8
newRight = newLeft + newSprite.width
newTop = newBottom + newSprite.height

# Highscores 
highscores = pyglet.resource.image('highscores.jpg')
scoresSprite = pyglet.sprite.Sprite(highscores)
scoresSprite.scale = 0.7178
scoresSprite.position = (0,-200)
scoresLeft, scoresBottom = 656,256
scoresRight = scoresLeft + scoresSprite.width
scoresTop = scoresBottom + scoresSprite.height

# Description
description = pyglet.resource.image('description.jpg')
descSprite = pyglet.sprite.Sprite(description)
descSprite.scale = 0.7178
descSprite.position = (0,-200)
descLeft, descBottom = 656,192.8
descRight = descLeft + descSprite.width
descTop = descBottom + descSprite.height

# Quit 
quitgame = pyglet.resource.image('quit.jpg')
quitSprite = pyglet.sprite.Sprite(quitgame)
quitSprite.scale = 0.7178
quitSprite.position = (0,-200)
quitLeft, quitBottom = 656,130
quitRight = quitLeft + quitSprite.width
quitTop = quitBottom + quitSprite.height

# Players Name
nicknames = pyglet.resource.image('nicknames.jpg')
nickSprite = pyglet.sprite.Sprite(nicknames)
nickSprite.scale = 0.7178
nickSprite.position = (0,-200)
nickLeft, nickBottom = 640,535
nickRight = nickLeft + nickSprite.width
nickTop = nickBottom + nickSprite.height
nickname_file = open("nickname.txt","r")
player = pyglet.text.Label(nickname_file.read(), font_name = 'Cenutry Gothic', font_size = 18, 
        x = (nickLeft+nickRight)/2, y = (nickTop+nickBottom)/2, anchor_x = 'center', anchor_y = 'center', bold = True)
nickname_file.close()

# Activity on the Main Menu
activity = pyglet.text.Label('', font_name='Century Gothic', font_size = 15, x = 240, y = 372.5, anchor_x='center', anchor_y='top', bold = True, color=(0,0,0,255))
activitySprite = pyglet.sprite.Sprite(pyglet.resource.image('activity.png'))
activitySprite.scale = 0.7
activitySprite.position = (0,-200)

# Mute and Unmute
unmute = pyglet.resource.image('unmute.jpg')
unmuteSprite = pyglet.sprite.Sprite(unmute)
unmuteSprite.scale = 0.7178
unmuteSprite.position = (18.8,20.4)

global current_loc
current_loc = 0

def current_location():
    return current_loc
    
def location_update(new_location):
    global current_loc
    current_loc = new_location

def nickname_update(new_name):
    player.text = new_name
    nickname_file = open("nickname.txt","w")
    nickname_file.write(new_name)
    nickname_file.close()

def get_nickname():
    return player.text[:len(player.text)-1]

def main_menu_mouse_press(x, y, button, modifiers,bgm):
    if button == mouse.LEFT:
        if y >= newBottom and y <= newTop and x >= newLeft and x <= newRight:
            location_update(4)
        elif y >= scoresBottom and y <= scoresTop and x >= scoresLeft and x <= scoresRight:
            location_update(3)
        elif y >= descBottom and y <= descTop and x >= descLeft and x <= descRight:
            location_update(2)
        elif y >= quitBottom and y <= quitTop and x >= quitLeft and x <= quitRight:
            pyglet.app.exit()
        elif y >= nickBottom and y<= nickTop and x >= nickLeft and x <= nickRight:
            location_update(1)
        elif x<=19.8+unmuteSprite.width and x>=18.8 and y<=20.4+unmuteSprite.height and y>=20.4:
            bgm.change_mute()

def main_menu_mouse_motion(x, y, button, modifiers):
    if y >= newBottom and y <= newTop and x >= newLeft and x <= newRight:
        activity.text = "Click to play a New Game."
        activitySprite.position = (60,288)
        newSprite.position = (newLeft,newBottom)
    elif y >= scoresBottom and y <= scoresTop and x >= scoresLeft and x <= scoresRight:
        activity.text = "Click to see Highscores."
        activitySprite.position = (60,288)
        scoresSprite.position = (scoresLeft,scoresBottom)
    elif y >= descBottom and y <= descTop and x >= descLeft and x <= descRight:
        activity.text = "Click to see Description."
        activitySprite.position = (60,288)
        descSprite.position = (descLeft,descBottom)
    elif y >= quitBottom and y <= quitTop and x >= quitLeft and x <= quitRight:
        activity.text = "Please don't Leave."
        activitySprite.position = (60,288)
        quitSprite.position = (quitLeft,quitBottom)
    elif y >= nickBottom and y<= nickTop and x >= nickLeft and x <= nickRight:
        nickSprite.position = (nickLeft,nickBottom)
    else:
        activity.text = ""
        newSprite.position = (0,-200)
        scoresSprite.position = (0,-200)
        descSprite.position = (0,-200)
        quitSprite.position = (0,-200)
        nickSprite.position = (0,-200)
        activitySprite.position = (0,-200)
    
def main_menu_draw(window,bgm):
    window.clear()
    bgSprite.draw()
    newSprite.draw()
    scoresSprite.draw()
    descSprite.draw()
    quitSprite.draw()
    nickSprite.draw()
    player.draw()
    activitySprite.draw()
    activity.draw()
    if bgm.mute_state():
        unmuteSprite.draw()