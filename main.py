import tkinter as tk

class Overlay(tk.Tk):
    def __init__(self, *a, **kw):
        tk.Tk.__init__(self, *a, **kw)
        self._set_window_attrs()
        self._set_alpha()

        # Load Assets
        self.spr_test = tk.PhotoImage(file='res/banana.png')
    def _set_window_attrs(self):
        self.title("Overlay")
        self.geometry("400x400+100+100")
        self.focus_force()
        self.wm_attributes("-topmost", True)
        self.overrideredirect(True)

        self.pos_x = 0
        self.pos_y = 0
    def _set_alpha(self):
        self.canvas = tk.Canvas(self, bg="black")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.config(highlightthickness=0)
        
        #self.canvas.create_image(self.pos_x,self.pos_y,image=self.spr_test)

        self.wm_attributes("-transparentcolor", "black")
    def run(self):
        self.mainloop()
    
# driver code
if __name__ == "__main__":
    Overlay().run()