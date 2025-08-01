import tkinter as tk

root = tk.Tk()
root.title("Combined Layout Example")

from_top = tk.Frame(root)
from_bottam = tk.Frame(root)

# Fixed "file" to "fill"
from_top.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
from_bottam.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

Label1 = tk.Label(from_top, text='Top Frame 1', bg='blue')
Label2 = tk.Label(from_bottam, text='Bottom Frame 2', bg='pink')
Label3 = tk.Label(from_bottam, text='Bottom Frame 3', bg='red')
Label4 = tk.Label(from_bottam, text='Bottom Frame 4', bg='yellow')

Label1.pack(side=tk.LEFT)
Label2.pack(side=tk.RIGHT)

# Using grid on same widget as pack causes issues. Avoid mixing them.
# For consistent layout, choose one layout manager: either pack() or grid()

# Option 1: Use pack for all
Label3.pack(side=tk.LEFT)
Label4.pack(side=tk.LEFT)

# Option 2: Use grid for all inside from_bottam
# Comment the above 3 lines and do this instead:
# Label2.grid(row=0, column=0)
# Label3.grid(row=0, column=1)
# Label4.grid(row=0, column=2)

root.mainloop()
