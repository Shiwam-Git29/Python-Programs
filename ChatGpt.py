import tkinter as tk

# Function to update expression
def press(key):
    global expression
    expression += str(key)
    input_text.set(expression)

# Function to calculate result
def equalpress():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Function to clear screen
def clear():
    global expression
    expression = ""
    input_text.set("")

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

expression = ""
input_text = tk.StringVar()

# Display screen
entry = tk.Entry(
    root,
    textvariable=input_text,
    font=("Arial", 18),
    bd=10,
    relief="sunken",
    justify="right"
)
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

# Button frame
frame = tk.Frame(root)
frame.pack()

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        tk.Button(frame, text=text, width=5, height=2,
                  font=("Arial", 14),
                  command=equalpress).grid(row=row, column=col, padx=5, pady=5)
