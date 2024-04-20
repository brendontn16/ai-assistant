import tkinter as tk
#import win32gui
#import win32con
#import win32api

class Overlay(tk.Tk):
    def __init__(self, *a, **kw):
        tk.Tk.__init__(self, *a, **kw)
        self._set_window_attrs()
        self._draw()

    def _set_window_attrs(self):
        self.title("Overlay")
        self.geometry("400x400+100+100")
        self.focus_force()
        self.wm_attributes("-topmost", True)
        self.overrideredirect(True)

        self.pos_x = 0
        self.pos_y = 0
    def _draw(self):
        self.canvas = tk.Canvas(self, bg="black")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.config(highlightthickness=0)

        self.spr_test = tk.PhotoImage(file='res/banana.png')
        self.canvas.create_image(self.pos_x,self.pos_y,image=self.spr_test,anchor="nw")

        self.wm_attributes("-transparentcolor", "black")

    # --Code for Clickthrough--

    # def set_clickthrough(hwnd, root):
    #     # Get window style and perform a 'bitwise or' operation to make the style layered and transparent, achieving
    #     # the clickthrough property
    #     l_ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    #     l_ex_style |= win32con.WS_EX_TRANSPARENT | win32con.WS_EX_LAYERED
    #     win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, l_ex_style)

    #     # Set the window to be transparent and appear always on top
    #     win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0, 0, 0), 190, win32con.LWA_ALPHA)  # transparent
    #     win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, root.winfo_x(), root.winfo_y(), 0, 0, 0)

    # def disable_clickthrough(hwnd, root):
    #     # Calling the function again sets the extended style of the window to zero, reverting to a standard window
    #     win32api.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, 0)
    #     # Remove the always on top property again, in case always on top was set to false in options
    #     win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, root.winfo_x(), root.winfo_y(), 0, 0, 0)

    def run(self):
        self.mainloop()
    
# driver code
if __name__ == "__main__":
    Overlay().run()