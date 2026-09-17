import tkinter as tk

# =========================
# WINDOW
# =========================

window = tk.Tk()
window.title("Dine Calculator")
window.geometry("400x650")
window.configure(bg="#000000")
window.resizable(False, False)

# =========================
# COLORS
# =========================

BLACK = "#000000"
DARK_GRAY = "#333333"
DARK_GRAY_HOVER = "#4A4A4A"

LIGHT_GRAY = "#A5A5A5"
LIGHT_GRAY_HOVER = "#C0C0C0"

WHITE = "#FFFFFF"

ORANGE = "#FF9F0A"
ORANGE_HOVER = "#FFB340"

GREEN = "#30D158"
GREEN_HOVER = "#55DD75"

RED = "#FF453A"
RED_HOVER = "#FF6259"

# =========================
# HISTORY
# =========================

history = []

# =========================
# CALCULATOR FUNCTIONS
# =========================

def add_to_display(value):

    operators = "+-*/"
    current = display.get()

    # Replace previous operator
    if value in operators and current:

        if current[-1] in operators:
            display.delete(len(current) - 1, tk.END)

    display.insert(tk.END, value)


def clear():

    display.delete(0, tk.END)


def backspace():

    current = display.get()

    if current:
        display.delete(len(current) - 1, tk.END)


def calculate():

    try:

        expression = display.get()

        if not expression:
            return

        if "%" in expression:
            expression = expression.replace("%", "/100")

        result = eval(expression)

        history.append(
            f"{display.get()} = {result}"
        )

        display.delete(0, tk.END)
        display.insert(0, str(result))

    except:

        display.delete(0, tk.END)
        display.insert(0, "Error")


# =========================
# HISTORY
# =========================

def show_history():

    history_window = tk.Toplevel(window)

    history_window.title("History")
    history_window.geometry("350x450")
    history_window.configure(bg=BLACK)
    history_window.resizable(False, False)

    title = tk.Label(
        history_window,
        text="History",
        font=("Arial", 24, "bold"),
        bg=BLACK,
        fg=WHITE
    )

    title.pack(pady=20)

    history_box = tk.Listbox(
        history_window,
        font=("Arial", 15),
        bg=DARK_GRAY,
        fg=WHITE,
        bd=0,
        highlightthickness=0
    )

    history_box.pack(
        expand=True,
        fill="both",
        padx=20,
        pady=10
    )

    if history:

        for calculation in history:

            history_box.insert(
                tk.END,
                calculation
            )

    else:

        history_box.insert(
            tk.END,
            "No calculations yet"
        )


# =========================
# BUTTON ANIMATION
# =========================

def press_effect(
    button,
    normal_color,
    hover_color,
    command
):

    button.config(
        bg="#666666",
        relief="sunken"
    )

    command()

    window.after(
        100,
        lambda: release_button(
            button,
            normal_color,
            hover_color
        )
    )


def release_button(
    button,
    normal_color,
    hover_color
):

    button.config(
        bg=hover_color,
        relief="flat"
    )

    window.after(
        100,
        lambda: button.config(
            bg=normal_color
        )
    )


# =========================
# HOVER EFFECT
# =========================

def hover_effect(
    button,
    normal_color,
    hover_color
):

    def mouse_enter(event):

        button.config(
            bg=hover_color
        )

    def mouse_leave(event):

        button.config(
            bg=normal_color
        )

    button.bind(
        "<Enter>",
        mouse_enter
    )

    button.bind(
        "<Leave>",
        mouse_leave
    )


# =========================
# DISPLAY
# =========================

display = tk.Entry(
    window,
    font=("Arial", 40),
    justify="right",
    bg=BLACK,
    fg=WHITE,
    insertbackground=WHITE,
    bd=0,
    highlightthickness=0
)

display.pack(
    fill="x",
    padx=20,
    pady=(35, 15),
    ipady=20
)

# =========================
# HISTORY BUTTON
# =========================

history_button = tk.Button(
    window,
    text="HISTORY",
    font=("Arial", 12, "bold"),
    command=show_history,
    bg=DARK_GRAY,
    fg=WHITE,
    activebackground=DARK_GRAY_HOVER,
    activeforeground=WHITE,
    bd=0,
    relief="flat"
)

history_button.pack(
    fill="x",
    padx=20,
    pady=(0, 12),
    ipady=6
)

hover_effect(
    history_button,
    DARK_GRAY,
    DARK_GRAY_HOVER
)

# =========================
# CALCULATOR BUTTONS
# =========================

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "%", "+"],
    ["(", ")", "←", "C"],
    ["="]
]

# =========================
# CREATE BUTTONS
# =========================

for row in buttons:

    frame = tk.Frame(
        window,
        bg=BLACK
    )

    frame.pack(
        expand=True,
        fill="both",
        padx=15
    )

    for button_text in row:

        # =====================
        # COMMAND
        # =====================

        if button_text == "=":

            command = calculate

        elif button_text == "C":

            command = clear

        elif button_text == "←":

            command = backspace

        else:

            command = lambda value=button_text: add_to_display(value)

        # =====================
        # COLORS
        # =====================

        if button_text in [
            "+",
            "-",
            "*",
            "/"
        ]:

            normal_color = ORANGE
            hover_color = ORANGE_HOVER

        elif button_text == "=":

            normal_color = GREEN
            hover_color = GREEN_HOVER

        elif button_text in [
            "C",
            "←"
        ]:

            normal_color = RED
            hover_color = RED_HOVER

        elif button_text in [
            "(",
            ")",
            "%"
        ]:

            normal_color = LIGHT_GRAY
            hover_color = LIGHT_GRAY_HOVER

        else:

            normal_color = DARK_GRAY
            hover_color = DARK_GRAY_HOVER

        # =====================
        # TEXT COLOR
        # =====================

        if button_text in [
            "(",
            ")",
            "%"
        ]:

            text_color = BLACK

        else:

            text_color = WHITE

        # =====================
        # CREATE BUTTON
        # =====================

        button = tk.Button(
            frame,
            text=button_text,
            font=("Arial", 20, "bold"),
            bg=normal_color,
            fg=text_color,
            activebackground=hover_color,
            activeforeground=text_color,
            bd=0,
            relief="flat"
        )

        button.config(
            command=lambda
            b=button,
            c=command,
            normal=normal_color,
            hover=hover_color:

            press_effect(
                b,
                normal,
                hover,
                c
            )
        )

        button.pack(
            side="left",
            expand=True,
            fill="both",
            padx=5,
            pady=5
        )

        hover_effect(
            button,
            normal_color,
            hover_color
        )


# =========================
# KEYBOARD CONTROLS
# =========================

def keyboard_input(event):

    key = event.keysym
    char = event.char

    # =====================
    # NUMBERS
    # =====================

    if char in "0123456789":

        add_to_display(char)

    # =====================
    # PLUS
    # Shift + =
    # =====================

    elif key == "equal" and (event.state & 0x0001):

        add_to_display("+")

    # =====================
    # MINUS
    # =====================

    elif char == "-":

        add_to_display("-")

    # =====================
    # MULTIPLY
    # Shift + 8
    # =====================

    elif char == "*":

        add_to_display("*")

    # =====================
    # DIVIDE
    # =====================

    elif char == "/":

        add_to_display("/")

    # =====================
    # PERCENT
    # Shift + 5
    # =====================

    elif char == "%":

        add_to_display("%")

    # =====================
    # DECIMAL
    # =====================

    elif char == ".":

        add_to_display(".")

    # =====================
    # PARENTHESES
    # =====================

    elif char == "(":

        add_to_display("(")

    elif char == ")":

        add_to_display(")")

    # =====================
    # ENTER
    # =====================

    elif key in [
        "Return",
        "KP_Enter"
    ]:

        calculate()

    # =====================
    # BACKSPACE
    # =====================

    elif key == "BackSpace":

        backspace()

    # =====================
    # ESCAPE
    # =====================

    elif key == "Escape":

        clear()


# Activate keyboard
window.bind(
    "<Key>",
    keyboard_input
)

window.focus_set()

# =========================
# START APPLICATION
# =========================

window.mainloop()