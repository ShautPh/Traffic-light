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

#Graphic street
canvas.create_image(400, 400, image=street)
canvas.create_image(400, 400, image=street2)


# the first root
canvas.create_rectangle(200,100,290,290, fill="black")
y = 110 
for i in range(3):
    canvas.create_oval(220,y,270, y+50, fill="gray")
    y += 60
def light_green_1():
    canvas.delete("light1")
    canvas.create_oval(220,110,270, 160, fill="green", tags="light1")
    canvas.after(6000,light_yellow_1)
    drivingD()
    drivingU()
def light_yellow_1():
    canvas.delete("light1")
    canvas.create_oval(220,170,270, 220, fill="yellow", tags="light1")
    canvas.after(3000,light_red_1)
def light_red_1():
    canvas.delete("light1")
    canvas.create_oval(220,230,270, 280, fill="red", tags="light1")
    canvas.after(6000,light_green_1)
canvas.after(600,light_red_1)


# # the second root
canvas.create_rectangle(510,100,600,290, fill="black")
y = 110
for i in range(3):
    canvas.create_oval(530,y,580, y+50, fill="gray")
    y += 60

def light_green_2():
    canvas.delete("light2")
    canvas.create_oval(530,110,580, 160, fill="green", tags="light2")
    canvas.after(6000,light_yellow_2)
    drivingR()
    drivingL()

def light_yellow_2():
    canvas.delete("light2")
    canvas.create_oval(530,170,580, 220, fill="yellow", tags="light2")
    canvas.after(3000,light_red_2)

def light_red_2():
    canvas.delete("light2")
    canvas.create_oval(530,230,580, 280, fill="red", tags="light2")
    canvas.after(6000,light_green_2)
canvas.after(600,light_green_2)


# the third root
canvas.create_rectangle(200,510,290,700, fill="black")
y = 520
for i in range(3):
    canvas.create_oval(220,y,270, y+50, fill="gray")
    y += 60
def light_red_3():
    canvas.delete("light3")
    canvas.create_oval(220,520,270, 570, fill="red", tags="light3")
    canvas.after(6000,light_green_3)
def light_yellow_3():
    canvas.delete("light3")
    canvas.create_oval(220,580,270, 630, fill="yellow", tags="light3")
    canvas.after(3000,light_red_3)
def light_green_3():
    drivingR()
    drivingL()
    canvas.delete("light3")
    canvas.create_oval(220,640,270, 690, fill="green", tags="light3")
    canvas.after(6000,light_yellow_3)
canvas.after(600,light_green_3)


# # the fourth root
canvas.create_rectangle(510,510,600,700, fill="black")
y = 520
for i in range(3):
    canvas.create_oval(530,y,580, y+50, fill="gray")
    y += 60
def red4():
    canvas.delete("light4")
    canvas.create_oval(530,520,580, 570, fill="red", tags="light4")
    canvas.after(6000,green4)
def yellow4():
    canvas.delete("light4")
    canvas.create_oval(530,580,580, 630, fill="yellow", tags="light4")
    canvas.after(3000,red4)

def green4():
    canvas.delete("light4")
    canvas.create_oval(530,640,580, 690, fill="green", tags="light4")
    canvas.after(6000,yellow4)
    drivingU()
    drivingD()
canvas.after(600,red4)

myCar1 = canvas.create_image(0, 450, image=car)
myCar2 = canvas.create_image(750, 350, image=carR)
myCar3 = canvas.create_image(450, 640, image=carU)
myCar4 = canvas.create_image(350, 40, image=carD)

# Driving left 
def drivingL():
    global myCar1
    pos = canvas.coords(myCar1)
    print(pos)
    if pos[0] < 900:
        canvas.move(myCar1, 15, 0)
    else:
        myCar1 = canvas.create_image(0, 450, image=car)
    canvas.after(100, drivingL)
    
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
    canvas.after(110, drivingU)
    
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


canvas.pack(expand=True,fill='both')
frame.pack(expand=True,fill='both')

window.mainloop()