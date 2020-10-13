from tkinter import *
import numpy as np
from scipy.integrate import odeint
#..............................Global variables 
RunAll=True
RunIter=False
#..............................Interaction funcions
def StartStop():
    global RunIter
    RunIter=not RunIter
    if RunIter:
        StartButton['text']='Stop'
    else:
        StartButton['text']='Restart'
def StopAll():
    global RunAll
    RunAll=False
#..............................Canvas data
delay=30
ButtWidth=9
cw=800
ch=400
#............................. Physical parameters
x0=50
l=200
dt=0.1
#.............................. Initial conditions
rad=20
oy=ch/2
x1=l-x0
v1=0
x2=2*l+2*x0
v2=0
x3=3*l+x0
v3=0
#.............................. Variable and parameter vectors
y=[x1,v1,x2,v2,x3,v3]
params=[l]
#.............................. System of equations
def dfdt(y,t,params):
    x1,v1,x2,v2,x3,v3=y
    l,=params
    derivs=[v1,-2*x1+x2,v2,x1-2*x2+x3,v3,x2-2*x3+4*l]
    return derivs
#.............................. Create root window
root=Tk()
root.title('Coupled oscillators')
#.............................. Add canvas to root window
canvas=Canvas(root,width=cw,height=ch,background='#ffffff')
canvas.grid(row=0,column=0)
#.................................. Add toolbar to root window
toolbar=Frame(root)
toolbar.grid(row=0,column=1,sticky=N)
#.................................. Toolbar buttons
nr=0
StartButton=Button(toolbar,text='Start',command=StartStop,width=ButtWidth)
StartButton.grid(row=nr,column=0,sticky=W)
nr+=1
ExitButton=Button(toolbar,text='Exit',command=StopAll,width=ButtWidth)
ExitButton.grid(row=nr,column=0,sticky=W)
#.................................. 
t=[0.0,dt]
#.................................. Main Loop
while RunAll:
    #.................................. Draw oscillator
    canvas.delete(ALL)
    canvas.create_line(0,oy,x1,oy,fill='black')
    canvas.create_oval(x1-rad,oy-rad,x1+rad,oy+rad,fill='Red')
    canvas.create_line(x1,oy,x2,oy,fill='black')
    canvas.create_oval(x2-rad,oy-rad,x2+rad,oy+rad,fill='Green')
    canvas.create_line(x2,oy,x3,oy,fill='black')
    canvas.create_oval(x3-rad,oy-rad,x3+rad,oy+rad,fill='Blue')
    canvas.create_line(x3,oy,cw,oy,fill='black')
    canvas.update()
    if RunIter:
        psoln=odeint(dfdt,y,t,args=(params,))
        x1=psoln[1,0]
        v1=psoln[1,1]
        x2=psoln[1,2]
        v2=psoln[1,3]
        x3=psoln[1,4]
        v3=psoln[1,5]
        #.................................. Update vector
        y=[x1,v1,x2,v2,x3,v3]
    canvas.after(delay)

root.destroy()