from tkinter import Tk,Canvas,ALL
import numpy as np

root=Tk()
root.title('Ejercicio 7.1')

cw=800
ch=640

canvas=Canvas(root,width=cw,height=ch,background='white')
canvas.grid(row=0,column=0)

delay=10
rad=160
color='red'
x=cw/2
y=ch/2
dt=0.1
t=0
omega=0.1
while True:
    canvas.delete(ALL)
    u1=rad*np.cos(t*omega-np.pi/4.-np.pi/2)
    v1=rad*np.sin(t*omega-np.pi/4.-np.pi/2)
    u2=rad*np.cos(t*omega-np.pi/4.)
    v2=rad*np.sin(t*omega-np.pi/4.)
    u3=rad*np.cos(t*omega+np.pi/4.)
    v3=rad*np.sin(t*omega+np.pi/4.)
    u4=rad*np.cos(t*omega+np.pi/4.+np.pi/2)
    v4=rad*np.sin(t*omega+np.pi/4.+np.pi/2)
    canvas.create_polygon(x+u1,y+v1,x+u2,y+v2,x+u3,y+v3,x+u4,y+v4,fill=color)
    canvas.update()
    t+=dt
    canvas.after(delay)