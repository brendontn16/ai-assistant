import tkinter as tk

root = tk.Tk()
root.title("Make a friend")
root.geometry("300x300")

def create_window():
    # Create new window
    top_window = tk.Toplevel(root)
    top_window.title("Top Window")
    top_window.geometry("200x200")
    top_window.wm_attributes("-topmost",True)
    top_window.wm_attributes('-alpha',0.1)

tk.Button(root, text = "Create Window", command = create_window).pack()

root.mainloop()