import tkinter as tk

def convert_to_fahrenheit():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{fahrenheit:.2f} °F")
    except ValueError:
        result_label.config(text="Enter valid number")

def convert_to_celsius():
    try:
        fahrenheit = float(entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{celsius:.2f} °C")
    except ValueError:
        result_label.config(text="Enter valid number")

# GUI window setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")

# Input field
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Buttons
btn1 = tk.Button(root, text="Convert to Fahrenheit", command=convert_to_fahrenheit)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Convert to Celsius", command=convert_to_celsius)
btn2.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
