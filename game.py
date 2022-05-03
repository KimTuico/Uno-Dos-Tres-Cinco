import pyglet                                                   #version 1.5.23
from home_screen_module import main_menu_draw
from home_screen_module import main_menu_mouse_press
from home_screen_module import main_menu_mouse_motion
from home_screen_module import current_location
from menu_module import nickname_draw
from menu_module import nickname_key_press
from menu_module import description_draw
from menu_module import description_mouse_press
from menu_module import highscore_draw
from menu_module import highscore_mouse_press
from game_module import game_draw
from game_module import game_mouse_motion
from game_module import game_mouse_press
from game_module import updates
from game_module import try_again_mouse_motion
from game_module import try_again_mouse_press
from game_module import try_again_draw

current_loc = current_location()  
global prev_loc 
prev_loc = current_loc   
    
pyglet.resource.path = ["resources"]
pyglet.resource.reindex()

# This is the pyglet window.
window = pyglet.window.Window(1024,768, "Uno, Dos, Tres, CINCO!")
logo = pyglet.resource.image('logo.jpg')
window.set_icon(logo)

muted_file = open("muted.txt","r")
muted = False if muted_file.read() == "False" else True
muted_file.close()

class background_music():
    def __init__(self):
        self.current_music = 0
        self.mute = muted
        
        self.menu = pyglet.resource.media('UP Main Menu.wav')
        #self.loops = pyglet.media.SourceGroup(self.menu.audio_format, None)        #old version of pyglet
        #self.loops.queue(self.menu)
        #self.loops.loop = True 
        self.mplayer = pyglet.media.Player()
        self.mplayer.queue(self.menu)
        if not self.mute:
            self.mplayer.play()
        
        self.game = pyglet.resource.media('UP Game.wav')
        #self.looper = pyglet.media.SourceGroup(self.game.audio_format, None)
        #self.looper.queue(self.game)
        #self.looper.loop = True 
        self.gplayer = pyglet.media.Player()
        self.gplayer.queue(self.game)
    
    def change_music(self):
        if not self.mute:
            self.current_music = 1 - self.current_music
            if self.current_music == 0:
                self.gplayer.pause()
                self.mplayer.play()
            else:
                self.mplayer.pause()
                self.gplayer.play()
        
    def change_mute(self):
        if self.mute:
            self.mute = False
            muted_file = open("muted.txt","w")
            muted_file.write("False")
            muted_file.close()
            self.mplayer.play()
        else:
            self.mute = True
            muted_file = open("muted.txt","w")
            muted_file.write("True")
            muted_file.close()
            self.mplayer.pause()
    
    def mute_state(self):
        return self.mute
    
@window.event
def on_mouse_press(x, y, button, modifiers):
    current_loc = current_location()
    if current_loc == 0:                                    # main menu
        main_menu_mouse_press(x, y, button, modifiers,bgm)  
    elif current_loc == 2:                                  # description
        description_mouse_press(x, y, button, modifiers)
    elif current_loc == 3:
        highscore_mouse_press(x, y, button, modifiers)
    elif current_loc == 4:
        game_mouse_press(x, y, button, modifiers)
    elif current_loc == 5:
        try_again_mouse_press(x, y, button, modifiers)
    
@window.event
def on_mouse_motion(x, y, button, modifiers):
    current_loc = current_location()
    if current_loc == 0:                                    # main menu
        main_menu_mouse_motion(x, y, button, modifiers)
    elif current_loc == 4:
        game_mouse_motion(x, y, button, modifiers)
    elif current_loc == 5:
        try_again_mouse_motion(x, y, button, modifiers)
    
@window.event
def on_key_press(symbol, modifiers):
    current_loc = current_location()
    if current_loc == 1:                                    # nickname
        nickname_key_press(symbol, modifiers) 

@window.event
def on_draw():
    current_loc = current_location()
    if current_loc == 0:                                    # main menu
        main_menu_draw(window, bgm)
    elif current_loc == 1:                                  # nickname
        nickname_draw(window)
    elif current_loc == 2:                                  # description
        description_draw(window)
    elif current_loc == 3:
        highscore_draw(window)
    elif current_loc == 4:
        game_draw(window)
    elif current_loc == 5:
        try_again_draw(window)
            
def update(dt):
    global prev_loc
    current_loc = current_location()
    if (prev_loc == 0 and current_loc == 4) or ( (prev_loc == 4 or prev_loc == 5) and current_loc == 0):
        bgm.change_music()
    prev_loc = current_loc
    if current_loc == 4:
        updates(dt,bgm)
    
bgm = background_music()
pyglet.clock.schedule_interval(update, 1./120) 
pyglet.app.run()