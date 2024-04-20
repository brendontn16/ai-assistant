from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from random import randrange, random
from numpy import sign, sinc
from math import sin, cos, pi

sprites = { # Dictionary of all the sprites that can be loaded.
  "idle": 'res/yalloIdle.png',
  "yap": 'res/yalloYap.gif',
  "banana": 'res/banana.png',
}
sprite_index = "yap" #Current sprite

def getMeOut():
   exit()
    

class Yallo(tk.Tk):
    def __init__(self, *a, **kw):
        tk.Tk.__init__(self, *a, **kw)

        #Setting up some important variables that determines Yallo's position.
        self.pos_x = 500
        self.pos_y = 250



        self._load_assets() # Loads assets first (can be re-run)
        self._set_window_attrs() # Configures window
        self._draw() # Draws to the window

        self._reset_target_position()
        self._tick()

    def _load_assets(self):
        img = Image.open(sprites[sprite_index])
        self.sprite_width = img.width
        self.sprite_height = img.height
        self.anim_frames = []
        self.anim_index = 0
        self.anim_delay = 50
        if img.format == "GIF":
            for i in range(img.n_frames):
                self.anim_frames.append(tk.PhotoImage(file = sprites[sprite_index], format = f"gif -index {i}"))
        elif img.format == "PNG":
            self.anim_frames.append(tk.PhotoImage(file = sprites[sprite_index]))
        else:
            self.anim_frames.append(tk.PhotoImage(file = sprites["banana"]))


    def _set_window_attrs(self):
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

        self.after(6000,self._stop_walking)
        self.after(30000,self._reset_target_position)

    def _tick(self):   
        if ((self.pos_x + self.dir_x > self.screen_width - self.sprite_width) | (self.pos_x + self.dir_x < 0) | (self.pos_y + self.dir_y > self.screen_height - self.sprite_height) | (self.pos_y + self.dir_y < 0) == False):
            self.pos_x += self.dir_x
            self.pos_y += self.dir_y
            self.canvas.moveto(self.yallo,self.pos_x,self.pos_y)
        else:
            self._reset_target_position()
        self.after(6,self._tick)

    def _stop_walking(self):
        self.dir_x, self.dir_y = 0, 0

    def _draw(self):
        self.canvas = tk.Canvas(self, bg="green")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.config(highlightthickness=0)

        self.yallo = self.canvas.create_image(self.pos_x, self.pos_y, image=self.anim_frames[0], anchor="nw")
        self.animate()
        
        B = Button(self.canvas, text ="Escape", command = getMeOut)
        B.place(x=self.pos_x-20, y=self.pos_y-10)

        self.wm_attributes("-transparentcolor", "green")
    
    def animate(self):
        self.anim_index = (self.anim_index + 1) % len(self.anim_frames)
        self.canvas.itemconfig(self.yallo, image=self.anim_frames[self.anim_index])
        self.after(self.anim_delay, self.animate)
        
    def run(self):
        self.mainloop()
    
# driver code
if __name__ == "__main__":
    Yallo().run()