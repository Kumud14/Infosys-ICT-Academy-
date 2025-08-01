import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("My Tkinter App")

# ✅ Open the image with PIL
img = Image.open("image.png")
icon = ImageTk.PhotoImage(img)

# ✅ Set it as window icon
root.iconphoto(True, icon)

root.geometry("300x200")
tk.Label(root, text="Icon set successfully!").pack(pady=50)

root.mainloop()
