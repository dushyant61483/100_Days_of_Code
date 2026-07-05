from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark = 1
time = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global reps
    reps = 0
    window.after_cancel(time)
    canvas.itemconfig(timer_text, text = "00:00")
    heading.config(text = "Timer", bg = YELLOW )
    tick.config(text = "")
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        timer(long_break_sec)
        heading.config(text = "Long Break", bg = RED )
    elif reps%2 == 0:
        timer(short_break_sec)
        heading.config(text = "Short Break",bg = PINK )
    else:
        timer(work_sec)
        heading.config(text = "Working Time",bg = YELLOW )


def timer(count):
    global time
    global checkmark
    count_min = math.floor(count / 60 )
    count_sec = math.floor(count % 60 )
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    if count_min < 10:
        count_min = "0" + str(count_min)
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        time = window.after(1000,timer , count-1)
    else:
        start_timer()
        checkmark += 1
        tick.config(text = "✓"*int(checkmark/2))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Pomodoro Application")
window.config(padx=100, pady=50 , background = YELLOW)


canvas = Canvas(width = 200 , height = 224 , background = YELLOW , highlightthickness = 0)
tomato_png = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_png)
timer_text = canvas.create_text(102,126 , text = "00:00" , font = (FONT_NAME, 35, "bold") , fill ="white")
canvas.grid(row = 1, column = 1)


heading = Label(window , text = "Timer" , font=("Courier", 30) , fg = GREEN , bg = YELLOW)
heading.grid(row = 0 , column = 1)

space = Label(window , text = " ")
space.grid(row = 2 , column = 1)

tick = Label(window , text = ""  , font = ("Courier", 30) , fg = GREEN , bg = YELLOW)
tick.grid(row = 3 , column = 1)
start_button = Button(window , text = "Start" , command= start_timer)
start_button.grid(row = 3 , column = 0)

reset_button = Button(window , text = "Reset" , command = reset)
reset_button.grid(row = 3 , column = 2)


window.mainloop()