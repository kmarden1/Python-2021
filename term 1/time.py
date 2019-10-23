import time
import calendar
from tkinter import*
from tkinter import ttk
from tkinter import font


def current_time():
    totalSeconds = calendar.timegm(time.gmtime())
    currentSecond = totalSeconds%60

    totalMinutes = totalSeconds//60
    currentMinute = totalMinutes%60

    totalHours = totalMinutes//60
    currentHour = (totalHours%24)-6

    am_pm = ""
    if currentHour>=12:
        am_pm = "PM"
    if currentHour==0:
        currentHour+currentHour+12
    else:
        am_pm= "AM"
        if currentHour==0:
            currentHour=currentHour+12


    timex = str(currentHour)+":"+str(currentMinute)+":"+str(currentSecond)+" "+(am_pm)
    return timex
def show_time():
    time = current_time()
    txt.set(time)
    root.after(1000, show_time)

root = Tk()

# set window size
root.geometry("500x200")
root.configure(background="blue")

root.after(1000, show_time)
fnt=font.Font(family='helvetica', size=60, weight='bold')
txt=StringVar()



lbl=ttk.Label(root, textvariable=txt, font=fnt, foreground="black", background="blue")
lbl.place(relx=0.5, rely=0.5, anchor= CENTER)


root.mainloop()
