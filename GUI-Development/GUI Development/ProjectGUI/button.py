import tkinter as tk
def on_button_click():
    Label.config(text='Button Clicked')
    
root = tk.Tk()
root.title("simple GUI")
root.geometry('300x300')

Label = tk.Label(root, text="Click the button", bg="lightblue")
Label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

root.mainloop()
    
