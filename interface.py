from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

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
        self._load_assets() # Loads assets first (can be re-run)
        self._set_window_attrs() # Configures window
        self._draw() # Draws to the window

    def _load_assets(self):
        img = Image.open(sprites[sprite_index])
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
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.geometry("{}x{}+{}+{}".format(screenWidth, screenHeight, 0, 0))
        self.focus_force()
        self.wm_attributes("-topmost", True)
        self.overrideredirect(True)

        self.pos_x = 500
        self.pos_y = 250
    
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