from tkinter import *
import tkinter as tk
screenOffset = 400

def getMeOut():
   exit()

class Overlay(tk.Tk):
    def __init__(self, *a, **kw):
        tk.Tk.__init__(self, *a, **kw)
        self._set_window_attrs()
        self._set_alpha()


    def _set_window_attrs(self):
        self.title("Overlay")
        screenWidth = self.winfo_screenwidth() - screenOffset
        screenHeight = self.winfo_screenheight() - screenOffset
        self.geometry("400x400+{}+{}".format(screenWidth,screenHeight))
        self.focus_force()
        self.wm_attributes("-topmost", True)
        self.overrideredirect(True)

        self.pos_x = 0
        self.pos_y = 0
    def _set_alpha(self):
        self.canvas = tk.Canvas(self, bg="black")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.config(highlightthickness=0)

        self.spr_test = tk.PhotoImage(file='res/banana.png')
        self.canvas.create_image(self.pos_x,self.pos_y,image=self.spr_test,anchor="nw")
        B = Button(self.canvas, text ="Escape", command = getMeOut)
        B.place(x=50,y=100)

        self.wm_attributes("-transparentcolor", "black")
    def run(self):
        self.mainloop()
    
# driver code
if __name__ == "__main__":
    Overlay().run()