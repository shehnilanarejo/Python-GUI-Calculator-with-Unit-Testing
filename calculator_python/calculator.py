import tkinter as tk
from tkinter import messagebox
import calculator

# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

# gui_calculator.py

def calculate(operation):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        
        if operation == "Add":
            result = calculator.add(a, b)
        elif operation == "Subtract":
            result = calculator.subtract(a, b)
        elif operation == "Multiply":
            result = calculator.multiply(a, b)
        elif operation == "Divide":
            result = calculator.divide(a, b)
        else:
            result = "Invalid Operation"

        result_label.config(text=f"Result: {result}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("500x400")  # Increased window size
root.resizable(True, True)  # Allow resizing
root.config(bg="lightyellow")  # Set background color to light yellow

# Title Label
title_label = tk.Label(root, text="Basic Calculator", font=("Arial", 16), bg="lightyellow", fg="darkblue")
title_label.pack(pady=20)

# Input for first number
tk.Label(root, text="Enter first number:", bg="lightyellow", font=("Arial", 12)).pack(pady=5)
entry1 = tk.Entry(root, font=("Arial", 12), width=20)
entry1.pack(pady=5)

# Input for second number
tk.Label(root, text="Enter second number:", bg="lightyellow", font=("Arial", 12)).pack(pady=5)
entry2 = tk.Entry(root, font=("Arial", 12), width=20)
entry2.pack(pady=5)

# Operation buttons
button_frame = tk.Frame(root, bg="lightyellow")
button_frame.pack(pady=10)

# Create buttons for operations
operations = ["Add", "Subtract", "Multiply", "Divide"]
for operation in operations:
    button = tk.Button(button_frame, text=operation, command=lambda op=operation: calculate(op), width=12, font=("Arial", 12), bg="lightblue", relief="solid")
    button.pack(side=tk.LEFT, padx=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=lambda: calculate("Custom"), width=20, font=("Arial", 12), bg="lightgreen", relief="solid")
calculate_button.pack(pady=15)

# Result label
result_label = tk.Label(root, text="Result: ", bg="lightyellow", font=("Arial", 12), fg="darkgreen")
result_label.pack(pady=10)

root.mainloop()

