from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
resp = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    label.config(text='Timer', fg=GREEN)
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text='00:00')
    global resp
    resp = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global resp
    resp += 1
    work_sec = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    if resp % 8 == 0:
        label.config(text='break', fg=RED)
        count_down(7)
    elif resp % 2 == 0:
        label.config(text='break', fg=PINK)
        count_down(5)
    else:
        label.config(text='work', fg=GREEN)
        count_down(10)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = int(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = "0" + str(seconds)
    if minutes < 10:
        minutes = "0" + str(minutes)

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(resp//2):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodora')
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'), highlightthickness=0)
label.grid(column=1, row=0)

tomato_img = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start = Button(text='Start', highlightthickness=0, bg=YELLOW, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text='Reset', highlightthickness=0, bg=YELLOW, command=reset_timer)
reset.grid(column=2, row=2)

check_mark = Label(fg=GREEN, font=(FONT_NAME, 10, 'bold'), bg=YELLOW, highlightthickness=0)
check_mark.grid(column=1, row=3)

window.mainloop()
