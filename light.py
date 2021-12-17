import tkinter as tk
from tkinter import font
window = tk.Tk()
window.geometry("800x700")
frame = tk.Frame()
frame.master.title("Traffic Lights")

canvas = tk.Canvas(frame)

# The Roads
canvas.create_text(400,60,text="Traffic Light Loading...", fill="black", font=("Purisa",20,font.BOLD))
canvas.create_rectangle(300,100,500,700, fill="gray")
canvas.create_rectangle(10,300,790,500, fill="gray")

canvas.create_rectangle(200,100,290,290, fill="black")
y = 110 
for i in range(3):
    canvas.create_oval(220,y,270, y+50, fill="gray")
    y += 60
canvas.create_rectangle(510,100,600,290, fill="black")


# the first root
def green1():
    canvas.delete("light")
    canvas.create_oval(220,110,270, 160, fill="green", tags="light")
    canvas.after(5000,red1)
def yellow1():
    canvas.delete("light")
    canvas.create_oval(220,170,270, 220, fill="yellow", tags="light")
    canvas.after(1000,green1)
def red1():
    canvas.delete("light")
    canvas.create_oval(220,230,270, 280, fill="red", tags="light")
    canvas.after(5000,yellow1)
canvas.after(100,red1)


# the second root
y = 110
for i in range(3):
    canvas.create_oval(530,y,580, y+50, fill="gray")
    y += 60

def green2():
    canvas.delete("light")
    canvas.create_oval(530,110,580, 160, fill="green", tags="light")
    canvas.after(6000,red2)

def yellow2():
    canvas.delete("light")
    canvas.create_oval(530,170,580, 220, fill="yellow", tags="light")
    canvas.after(2000,green2)

def red2():
    canvas.delete("light")
    canvas.create_oval(530,230,580, 280, fill="red", tags="light")
    canvas.after(6000,yellow2)
canvas.after(200,red2)


# the third root
canvas.create_rectangle(200,510,290,700, fill="black")
y = 520
for i in range(3):
    canvas.create_oval(220,y,270, y+50, fill="gray")
    y += 60
def green3():
    canvas.delete("light")
    canvas.create_oval(220,110,270, 160, fill="green", tags="light")
    canvas.after(5000,red3)
def yellow3():
    canvas.delete("light")
    canvas.create_oval(220,170,270, 220, fill="yellow", tags="light")
    canvas.after(1000,green3)
def red3():
    canvas.delete("light")
    canvas.create_oval(220,230,270, 280, fill="red", tags="light")
    canvas.after(5000,yellow3)
canvas.after(100,red3)



canvas.create_rectangle(510,510,600,700, fill="black")
y = 520
for i in range(3):
    canvas.create_oval(530,y,580, y+50, fill="gray")
    y += 60

canvas.pack(expand=True,fill='both')
frame.pack(expand=True,fill='both')

window.mainloop()