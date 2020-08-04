"""
The goal of this project is develop a simple calculator following Codemy.com tutorial

Tkinter Course - Create Graphic User Interfaces in Python Tutorial

https://www.youtube.com/watch?v=YXPyB4XeYLA

"""
from tkinter import *

root = Tk()
root.title("Simple Calculator")

#Create and Display Input Box
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Creating Functions

# When Numbers are Clicked
def button_click(number):
    current = e.get()
    new = str(current) + str(number)
    e.delete(0, END)
    e.insert(0, new)


# Clear Button
def button_clear():
    e.delete(0,END)

# Add Button
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "Add"
    f_num = float(first_number)
    e.delete(0,END)

# Divide Button
def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "Div"
    f_num = float(first_number)
    e.delete(0, END)

# Multiply Button
def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "Mul"
    f_num = float(first_number)
    e.delete(0,END)

# Subtraction Button
def button_sub():
    first_number = e.get()
    global f_num
    global math
    math="Sub"
    f_num = float(first_number)
    e.delete(0,END)

# Equal Button
def button_equal():
    second_number=float(e.get())
    e.delete(0, END)
    if math == "Add":
        sumation=f_num + second_number

    if math == "Sub":
        sumation = f_num - second_number

    if math == "Mul":
        sumation = f_num * second_number

    if math == "Div":
        sumation = f_num / second_number
    e.insert(0, sumation)


# Define Buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root,text="+",padx=40,pady=50,command=button_add)
button_sub = Button(root,text="-",padx=40,pady=20,command=button_sub)
button_mul = Button(root,text="*",padx=40,pady=20,command=button_mul)
button_div = Button(root,text="/",padx=40,pady=20,command=button_div)


button_equal = Button(root,text="=",padx=39,pady=50,command=button_equal)
button_clear = Button(root,text="Clear",padx=28,pady=20,command=button_clear)


# Display Buttons
button_clear.grid(row=2, column=0)
button_div.grid(row=2, column=1)
button_mul.grid(row=2, column=2)
button_sub.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_add.grid(row=3, column=3, rowspan=2)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)

button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)
button_equal.grid(row=5, column=3, rowspan=2)


button_0.grid(row=6, column=0)





#myButton = Button(root,text="Enter Name", command=myClick)


root.mainloop()