from tkinter import *
import tkinter as tk
<<<<<<< Updated upstream
from PIL import Image
from random import randrange
=======
from PIL import Image, ImageTk
from random import randrange, random
>>>>>>> Stashed changes
from math import sin, cos, pi
from tts import text_to_speech
from sys import exit
from win32gui import GetWindowText, GetForegroundWindow

# Constants to let Yallo know not to go over the edge (it's his hitbox in a way)
sprite_width, sprite_height = 160, 160

# Variables
messageDelay = 5000
Encouragement = """I fucking hate gaming laptops."""

# End Program
def getMeOut():
   exit(0)

# Initiates talking when button is pressed
def shoutingTime():
    print(text_to_speech(Encouragement))

    window = tk.Tk()
    window.wm_attributes("-topmost",True)
    window.wm_attributes('-alpha', 0.95)
    window.config(borderwidth=0)
    window.overrideredirect(1)
    window.geometry("500x100+{}+{}".format(round(friend.pos_x),round(friend.pos_y)))

    # Create text widget and specify size.
    friendSays = Text(window, height = 7, width = 52)
    friendSays.configure(font = ("Comic Sans MS", 14), wrap=WORD)
    
    # Friend chat window
    chatTitle = Label(window, text = "Friend Says")
    chatTitle.pack()
    friendSays.pack()
    friendSays.insert(tk.END, Encouragement)
    friendSays.focus_force()
    friendSays.after(messageDelay,window.destroy)

    if (friend.facing == 0):
        friend.sprite_index = "yap_l"
    else:
        friend.sprite_index = "yap_r"



# Friend overlay

class Yallo(tk.Tk):

    # Setup
    def __init__(self, *a, **kw):
        tk.Tk.__init__(self, *a, **kw)

        #Setting up some important variables regarding Yallo.
        self.pos_x = 500
        self.pos_y = 250
        self.sprite_index = "idle_l"    #Starting sprite
        self.facing = 0                 #0 for left, 1 for right
        self.anim_index = 0             #Basically a timer that determines the current frame in the gif.
        self.anim_delay = 50           #How fast the gif frames go

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

    counter = 0
    def _tick(self):   
        self.counter += 1
        # Bad solution to the problem of timing, but I don't have time to redo the movement code
        if (self.counter % 5000 == 0):
            print(GetWindowText(GetForegroundWindow()))



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
        

        # Escape button
        Escape = Button(self.canvas, text ="Escape", command = getMeOut)
        Escape.place(x=20, y=10)

        # Temp button for testing chat functionality
        T = Button(self.canvas, text ="Talk", command = shoutingTime)
        T.place(x=10,y=100)

        self.wm_attributes("-transparentcolor", "green")
    
    def animate(self):
        self.anim_index = (self.anim_index + 1) % len(self.sprites[self.sprite_index])
        self.canvas.itemconfig(self.yallo, image= self.sprites[self.sprite_index][self.anim_index])
        self.after(self.anim_delay, self.animate)
    
    def run(self):
        self.mainloop()
    
# Run it all. We create an object for Yallo so his variables can be referenced for tts to work
# Also Yallo is indeed your friend. :)
if __name__ == "__main__":
    friend = Yallo()
    friend.run()