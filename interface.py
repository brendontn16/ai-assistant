from tkinter import *
import tkinter as tk
from PIL import Image


def getMeOut():
   exit()

class Overlay(tk.Tk):
    def __init__(self, *a, **kw):
        tk.Tk.__init__(self, *a, **kw)
        self._load_assets()
        self._set_window_attrs()
        self._draw()

    def _load_assets(self):
        self.spr_idle = tk.PhotoImage(file='res/yalloIdle.png')

    def _set_window_attrs(self):
        self.title("Overlay")
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.geometry("{}x{}+{}+{}".format(screenWidth,screenHeight,0,0))
        self.focus_force()
        self.wm_attributes("-topmost", True)
        self.overrideredirect(True)

        self.pos_x = 500
        self.pos_y = 250
    def _draw(self):
        self.canvas = tk.Canvas(self, bg="green")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.config(highlightthickness=0)

        self.canvas.create_image(self.pos_x,self.pos_y,image=self.spr_idle,anchor="nw")
        B = Button(self.canvas, text ="Escape", command = getMeOut)
        B.place(x=self.pos_x-20,y=self.pos_y-10)

        self.wm_attributes("-transparentcolor", "green")
    def run(self):
        self.mainloop()
    
# driver code
if __name__ == "__main__":
    Overlay().run()