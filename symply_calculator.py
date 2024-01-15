import tkinter as tk
from math import sqrt


def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def perform_calculation():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the window
root = tk.Tk()
root.title("Calculator")

# Create the entry field
entry = tk.Entry(root, width=16, font=('Arial', 20), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Create the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+', '=',
    '//', '%','sqrt', 'pow',
    '(', ')', ','
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 16),
              command=lambda b=button: button_click(b) if b != '=' else perform_calculation()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the main loop
root.mainloop()