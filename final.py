import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.colorchooser


def clear_text():
    text.delete(0,tk.END)

    entry_num1.delete(0,tk.END)
    entry_num2.delete(0,tk.END)


# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def sub(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def mul(num1, num2):
    return num1 * num2

# Function to divide two numbers
def div(num1, num2):
    return num1 / num2

# Function to handle button click and perform the selected operation
def calculate():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        operation = select_operation.get()

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = sub(num1, num2)
        elif operation == "*":
            result = mul(num1, num2)
        elif operation == "/":
            result = div(num1, num2)
        else:
            result = "Invalid Operation"

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Invalid input")

# Create the main Tkinter window
root = tk.Tk()
text = tk.Entry(root)


# Set the width and height of the GUI window
window_width = 300
window_height = 300
root.geometry(f"{window_width}x{window_height}")

# Label and Entry for the first number
label_num1 = tk.Label(root, text="Enter first Number:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

# Label and Entry for the second number
label_num2 = tk.Label(root, text="Enter second Number:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Dropdown menu for selecting the operation
select_operation = tk.StringVar()
select_operation.set("+")
operation_choices = ["+", "-", "*", "/"]
operation_menu = tk.OptionMenu(root, select_operation, *operation_choices)
operation_menu.pack()

# Button to perform the calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Label to display the result
result_label = tk.Label(root, text="Result: ")

result_label.pack()








isYes=tkinter.messagebox.askyesno('Ask yes no',"Continue")
print(isYes)

isOk=tkinter.messagebox.askokcancel("Are you ok?","OK?")
print(isOk)


isYesNoCancel=tkinter.messagebox.askyesnocancel("ask yes no cancel","Yes, No, Cancel?")
print(isYesNoCancel)


name=tkinter.simpledialog.askstring("askstring","Enter your name")
print(name)


age=tkinter.simpledialog.askinteger("askinteger","Enter your age")
print(age)

weight=tkinter.simpledialog.askstring("askstring","Enter your password")
print(weight)

c=tkinter.colorchooser.askcolor()
print(c)



# Function to change the color and text of the button
def change_color():
    selected_color = color_var.get()
    button.config(bg=selected_color, text=f"{selected_color.capitalize()} Button")


color=print("Choose your favourite color in this box")
# Options for color choice
color_options = ["red", "blue", "green"]

# Variable to store the chosen color
color_var = tk.StringVar(root)
color_var.set(color_options[0])  # Default choice

# Option menu for selecting color
color_menu = tk.OptionMenu(root, color_var, *color_options)
color_menu.pack()

# Button to change color and text
button = tk.Button(root, text="Red Button", command=change_color, bg="red")
button.pack()

submit_button = tk.Button(root,text="Clear", command=clear_text, font=('Helvetica bold',10)).pack(pady=5)


root.mainloop()










