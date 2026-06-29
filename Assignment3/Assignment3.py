import tkinter as tk

# Conversion function
def convert(*args):
    try:
        mpg = float(mpg_var.get())
        kmpl = mpg * 0.425143707
        result_var.set(f"{kmpl:.3f}")
    except ValueError:
        result_var.set("")


# Create window
window = tk.Tk()
window.title("MPG to KM/L Converter")
window.geometry("300x150")

# Variables
mpg_var = tk.StringVar()
result_var = tk.StringVar()

mpg_var.trace_add("write", convert)

# Labels and Entry boxes
tk.Label(window, text="Miles per Gallon (MPG):").pack(pady=5)

mpg_entry = tk.Entry(window, textvariable=mpg_var)
mpg_entry.pack()

tk.Label(window, text="Kilometers per Liter (KM/L):").pack(pady=5)

result_entry = tk.Entry(window, textvariable=result_var, state="readonly")
result_entry.pack()

window.mainloop()
