import tkinter as tk

root = tk.Tk()
root.geometry("300x400")

label1 = tk.Label(root,text='Label 1',bg='red')
label1.grid(row=0,column=0)

label2 = tk.Label(root, text="Label 2",bg='green')
label2.grid (row=1,column=0)

root.mainloop()