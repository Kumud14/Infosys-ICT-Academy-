import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root,text='Label 1',bg='red')
label1.pack(fill=tk.BOTH,expand=True)

label2 = tk.Label(root, text="Label 2",bg='green')
label2.pack (fill=tk.BOTH,expand=True)

root.mainloop()