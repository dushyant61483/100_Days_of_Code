from tkinter import *
window = Tk()

window.title("Miles to Kilometer converter")
window.config(padx = 50, pady = 50)
window.minsize(400, 300)
window.maxsize(800,600)

# Entry
int_entry = Entry(window , width= 10 , font = ('arial', 20))
int_entry.grid(row = 0, column = 2)

# label
first = Label(window , text = " Miles", font = ('arial', 20))
first.grid(row = 0, column = 3)


second = Label(window , text = "is equal to", font = ('arial', 20))
second.grid(row = 1, column = 1)


answer = Label(window , text = '0', font = ('arial', 20))
answer.grid(row = 1, column = 2)

last = Label(window , text = " Kilometers" , font = ('arial', 20))
last.grid(row = 1, column = 3)


def convert():
    miles = int_entry.get()
    km = 1.609*float(miles)
    km = round(km, 2)
    answer["text"] = km

# Button
converter = Button(window , text = 'Convert' , command = convert , bg = "blue" , font = ('arial', 20))

converter.grid(row = 3 , column = 2)


window.mainloop()