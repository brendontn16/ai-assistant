from tkinter import *
import tkinter as tk

# Variables
xOffset = 600
yOffset = 600
messageDelay = 5000
Encouragement = """You're not being productive"""

# End Program
def getMeOut():
   exit()

# Initiates talking when button is pressed
def shoutingTime():
    window = tk.Tk()
    window.wm_attributes("-topmost",True)
    window.wm_attributes('-alpha', 0.95)
    window.config(borderwidth=0)
    window.overrideredirect(1)
    window.geometry("500x100+{}+{}".format(xOffset-210,yOffset-120))

    # Create text widget and specify size.
    friendSays = Text(window, height = 5, width = 52)
    friendSays.configure(font = ("Comic Sans MS", 14, "bold"), wrap=WORD)
    
    # Friend chat window
    chatTitle = Label(window, text = "Friend Says")
    chatTitle.pack()
    friendSays.pack()
    friendSays.insert(tk.END, Encouragement)
    friendSays.focus_force()
    friendSays.after(messageDelay,window.destroy)


# Friend overlay
class Overlay(tk.Tk):
    # Setup
    def __init__(self, *a, **kw):
        tk.Tk.__init__(self, *a, **kw)
        self._set_window_attrs()
        self._set_alpha()

    def _set_window_attrs(self):
        self.title("Overlay")
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.geometry("{}x{}+{}+{}".format(screenWidth,screenHeight,0,0))
        self.focus_force()
        self.wm_attributes("-topmost", True)
        self.overrideredirect(True)

        self.pos_x = xOffset
        self.pos_y = yOffset
    def _set_alpha(self):

        self.canvas = tk.Canvas(self, bg="green")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.config(highlightthickness=0)
        self.spr_test = tk.PhotoImage(file='res/yolloIdle.png')
        self.canvas.create_image(self.pos_x,self.pos_y,image=self.spr_test,anchor="nw")

        # Escape button
        Escape = Button(self.canvas, text ="Escape", command = getMeOut)
        Escape.place(x=self.pos_x-20,y=self.pos_y-10)

        # Temp button for testing chat functionality
        T = Button(self.canvas, text ="Talk", command = shoutingTime)
        T.place(x=10,y=100)

        self.wm_attributes("-transparentcolor", "green")

    def run(self):
        self.mainloop()
    
# driver code
if __name__ == "__main__":
    Overlay().run()