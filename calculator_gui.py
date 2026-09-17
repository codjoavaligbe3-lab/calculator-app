import tkinter as tk

window = tk.Tk()
window.title("COD Calculator")
window.geometry("400x600")

display = tk.Entry(
    window,
    font=("Arial", 28),
    justify="right",
    bd=10
)
display.pack(fill="x", padx=10, pady=10)


def add_to_display(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)

def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])


def calculate():
    try:
        expression = display.get()
        if "%" in expression: 
            expression = expression.replace("%", "/100")

        result = eval(expression)

        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "%", "+"],
    ["(", ")", "←", "C"],
    ["="]
]

for row in buttons:
    frame = tk.Frame(window)
    frame.pack(expand=True, fill="both")

    for button in row:
        if button == "=":
            command = calculate
        elif button == "C":
            command = clear
        elif button == "←":
            command = backspace
        else:
            command = lambda value=button: add_to_display(value)

        tk.Button(
            frame,
            text=button,
            font=("Arial", 20),
            command=command
        ).pack(side="left", expand=True, fill="both")



window.mainloop()