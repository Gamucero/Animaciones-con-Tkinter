from tkinter import Tk,Canvas,ALL
from random import random
import numpy as np

root=Tk()
root.title('Random Walk')

cw=800
ch=640

canvas=Canvas(root,width=cw,height=ch,background='white')
canvas.grid(row=0,column=0)

step=5
Nsteps=1000

delay=40
color='red'
z=x=cw/2
w=y=ch/2
line=[x,y,x,y]
line1=[z,w,z,w]
for i in range(Nsteps):
    canvas.delete(ALL)
    canvas.create_line(line,fill=color)
    canvas.create_line(line1,fill='green')
    canvas.update()
    if random()<0.5:
        x1=x+step
    else:
        x1=x-step
    if random()<0.5:
        y1=y+step
    else:
        y1=y-step
    line.append(x1)
    line.append(y1)
    x=x1
    y=y1

    if random()<0.5:
        z1=z+step
    else:
        z1=z-step
    if random()<0.5:
        w1=w+step
    else:
        w1=w-step
    line1.append(z1)
    line1.append(w1)
    z=z1
    w=w1
    canvas.after(delay)