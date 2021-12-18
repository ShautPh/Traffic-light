import tkinter as tk
from tkinter import PhotoImage, font
window = tk.Tk()
window.geometry("800x700")
frame = tk.Frame()
frame.master.title("Traffic Lights")

canvas = tk.Canvas(frame)

# Image 
street = PhotoImage(file="./img/road.png")
street2 = PhotoImage(file="./img/road2.png")
car = PhotoImage(file="./img/car.png")
carR = PhotoImage(file="./img/carR.png")
carU = PhotoImage(file="./img/carU.png")
carD = PhotoImage(file="./img/carD.png")

# The Roads
canvas.create_text(400,60,text="Traffic Light Loading...", fill="black", font=("Purisa",20,font.BOLD))
# canvas.create_rectangle(300,100,500,700, fill="gray") # Road
canvas.create_image(400, 400, image=street)

# canvas.create_rectangle(10,300,790,500, fill="gray")
canvas.create_image(400, 400, image=street2)

canvas.create_rectangle(200,100,290,290, fill="black")
y = 110 
for i in range(3):
    canvas.create_oval(220,y,270, y+50, fill="gray")
    y += 60
canvas.create_rectangle(510,100,600,290, fill="black")


# the first root
def green():
    canvas.delete("light")
    canvas.create_oval(220,110,270, 160, fill="green", tags="light")
    canvas.after(5000,red)
def yellow():
    canvas.delete("light")
    canvas.create_oval(220,170,270, 220, fill="yellow", tags="light")
    canvas.after(1000,green)
def red():
    canvas.delete("light")
    canvas.create_oval(220,230,270, 280, fill="red", tags="light")
    canvas.after(5000,yellow)

canvas.after(100,red)

y = 110
for i in range(3):
    canvas.create_oval(530,y,580, y+50, fill="gray")
    y += 60

canvas.create_rectangle(200,510,290,700, fill="black")
y = 520
for i in range(3):
    canvas.create_oval(220,y,270, y+50, fill="gray")
    y += 60

canvas.create_rectangle(510,510,600,700, fill="black")
y = 520
for i in range(3):
    canvas.create_oval(530,y,580, y+50, fill="gray")
    y += 60

myCar1 = canvas.create_image(150, 450, image=car)
myCar2 = canvas.create_image(750, 350, image=carR)
myCar3 = canvas.create_image(450, 640, image=carU)
myCar4 = canvas.create_image(350, 40, image=carD)

# Driving
# left 
def drivingL():
    global myCar1
    pos = canvas.coords(myCar1)
    print(pos)
    if pos[0] < 900:
        canvas.move(myCar1, 15, 0)
    else:
        myCar1 = canvas.create_image(150, 450, image=car)
    canvas.after(150, drivingL)
    
# Right
def drivingR():
    global myCar2
    pos = canvas.coords(myCar2)
    print(pos)
    if pos[0] > -50:
        canvas.move(myCar2, -15, 0)
    else:
        myCar2 = canvas.create_image(750, 350, image=carR)
    canvas.after(150, drivingR)
    
# Up
def drivingU():
    global myCar3
    pos = canvas.coords(myCar3)
    print(pos)
    if pos[1] > -50:
        canvas.move(myCar3, 0, -15)
    else:
        myCar3 = canvas.create_image(450, 640, image=carU)
    canvas.after(150, drivingU)
    
# Down
def drivingD():
    global myCar4
    pos = canvas.coords(myCar4)
    print(pos)
    if pos[1] < 800:
        canvas.move(myCar4, 0, 15)
    else:
        myCar4 = canvas.create_image(350, 40, image=carD)
    canvas.after(150, drivingD)
drivingR()
drivingL()
drivingU()
drivingD()

canvas.pack(expand=True,fill='both')
frame.pack(expand=True,fill='both')

window.mainloop()