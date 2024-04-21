from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from random import randrange, random
from numpy import sign, sinc
from math import sin, cos, pi

# Constants to let Yallo know not to go over the edge (it's his hitbox in a way)
sprite_width, sprite_height = 160, 160


def getMeOut():
   exit()
    

class Yallo(tk.Tk):
    def __init__(self, *a, **kw):
        tk.Tk.__init__(self, *a, **kw)

        #Setting up some important variables regarding Yallo.
        self.pos_x = 500
        self.pos_y = 250
        self.sprite_index = "idle_l"    #Starting sprite
        self.facing = 0                 #0 for left, 1 for right
        self.anim_index = 0             #Basically a timer that determines the current frame in the gif.
        self.anim_delay = 100           #How fast the gif frames go

        self.sprites = { # Preload all the sprites in a dictionary.
        "idle_l": self.load_asset('res/yalloIDLE.gif'),
        "yap_l": self.load_asset('res/yalloYAP.gif'),
        "walk_l": self.load_asset('res/yalloWALK.gif'),
        "idle_r": self.load_asset('res/yalloIDLE_R.gif'),
        "yap_r": self.load_asset('res/yalloYAP_R.gif'),
        "walk_r": self.load_asset('res/yalloWALK_R.gif'),
        "banana": self.load_asset('res/banana.png'),
        }

        self._set_window_attrs() # Configures window
        self._draw() # Draws to the window

        #Finally, kickstart these two autonomous functions
        self._reset_target_position() # Changes where the guy wants to go
        self._tick() # Runs almost every frame, makes him move.

    def load_asset(self, str): # Takes dictionary key as an argument, returns corresponding sprites
        img = Image.open(str)

        asset = []
        if img.format == "GIF":
            for i in range(img.n_frames):
                asset.append(tk.PhotoImage(file = str, format = f"gif -index {i}"))
        elif img.format == "PNG":
            asset.append(tk.PhotoImage(file = str))

        return asset


    def _set_window_attrs(self): # Configures window sizes and such (it takes up the whole screen actually)
        self.title("Overlay")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry("{}x{}+{}+{}".format(self.screen_width, self.screen_height, 0, 0))
        self.focus_force()
        self.wm_attributes("-topmost", True)
        self.overrideredirect(True)

    def _reset_target_position(self):
        self.target_x = randrange(self.screen_width)
        self.target_y = randrange(self.screen_height)
        direction = (self.target_y - self.pos_y) / (self.target_x - self.pos_x) * 180 / pi
        self.dir_x = sin(direction)
        self.dir_y = cos(direction)

        if (self.dir_x > 0):
            self.facing = 0
            self.sprite_index = "walk_l"
        else:
            self.facing = 1
            self.sprite_index = "walk_r"

        self.after(600,self._stop_walking)
        self.after(3000,self._reset_target_position)

    def _tick(self):   
        if ((self.pos_x + self.dir_x > self.screen_width - sprite_width) | (self.pos_x + self.dir_x < 0) | (self.pos_y + self.dir_y > self.screen_height - sprite_height) | (self.pos_y + self.dir_y < 0) == False):
            self.pos_x += self.dir_x
            self.pos_y += self.dir_y
            self.canvas.moveto(self.yallo,self.pos_x,self.pos_y)
        else:
            self._reset_target_position()
        self.after(1, self._tick)

    def _stop_walking(self): 
        self.dir_x, self.dir_y = 0, 0
        if (self.facing == 0):
            self.sprite_index = "idle_l"
        else:
            self.sprite_index = "idle_r"

    def _draw(self):
        self.canvas = tk.Canvas(self, bg="green")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.config(highlightthickness=0)

        self.yallo = self.canvas.create_image(self.pos_x, self.pos_y, image=self.sprites[self.sprite_index][0], anchor="nw")
        self.animate()
        
        B = Button(self.canvas, text ="Escape", command = getMeOut)
        B.place(x=20, y=10)

        self.wm_attributes("-transparentcolor", "green")
    
    def animate(self):
        self.anim_index = (self.anim_index + 1) % len(self.sprites[self.sprite_index])
        self.canvas.itemconfig(self.yallo, image= self.sprites[self.sprite_index][self.anim_index])
        self.after(self.anim_delay, self.animate)
        
    def run(self):
        self.mainloop()
    
# driver code
if __name__ == "__main__":
    Yallo().run()