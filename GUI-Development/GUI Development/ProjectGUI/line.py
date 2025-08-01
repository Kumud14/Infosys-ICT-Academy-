import tkinter as tk

root = tk.Tk()
root.title("Line Example")
root.geometry("500x400")

canvas = tk.Canvas(root,width=400,height=400)
canvas.pack()

canvas.create_line(50,50,200,50, fill='blue',width=3)
canvas.create_line(200,50,200,200, fill='red',width=5)

root.mainloop()