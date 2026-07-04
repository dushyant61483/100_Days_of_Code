# import tkinter as tk
#
# screen = tk.Tk()
# gui_title = screen.title("MY First App")
# screen.minsize(width = 500 , height = 400)
# screen.maxsize(width=1000 , height=1000)
#
#
# my_label = tk.Label(screen, text="Hello World", font=("Arial", 25))
# my_label.pack(side="top")
#
#
# def counting():
#     for i in range(10):
#         print(i)
#
#
# my_button1 = tk.Button(screen, text="Click to count to 9", command= counting)
# my_button1.pack()
#
# def change_label():
#     my_label["text"] = "Label Changed"
# label_change = tk.Button(screen , text = "Click me to change label" , command = change_label)
# label_change.pack()
#
#
# # Entry
# input = tk.Entry(width = 10)
# input.pack()
# def entry():
#     my_label["text"] = input.get()
#
# input_button = tk.Button(screen, text= "Click to print the input" , command = entry)
# input_button.pack()
# screen.mainloop()

from tkinter import *

screen = Tk()
screen.title("My GUI Using Grid")
screen.minsize(400, 300)
screen.maxsize(800, 600)
screen.config(padx = 100, pady = 100)

# Label
my_label = Label(screen, text="My GUI Using Grid")
my_label.grid(row = 0, column = 0 )
my_label.config(padx = 100, pady = 100)
# First Button
first = Button(screen, text="Hello", command=lambda: print("Hello"))
first.grid(row = 1, column = 1)

# Second Button
second = Button(screen, text="World", command=lambda: print("World"))
second.grid(row = 0, column = 3)

# Entry
input = Entry(width=40)
input.grid(row = 2, column = 4 )

screen.mainloop()
