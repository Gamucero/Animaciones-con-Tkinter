from tkinter import *
import numpy as np
from scipy.integrate import odeint
#..............................Global variables 
RunAll = True
RunIter = False
#..............................Interaction funcions
def StartStop():
    global RunIter
    RunIter = not RunIter
    if RunIter:
        StartButton['text']='Stop'
    else:
        StartButton['text']='Restart'
def StopAll():
    global RunAll
    RunAll = False
#..............................Canvas data
delay = 1
ButtWidth = 9
cw = 600
ch = 600
#............................. Physical parameters
m1 = 100.0
m2 = 20.0
l1 = 150
l2 = 100
g = 100.0
dt = 0.05
#.............................. Initial conditions
rad = 10
ox = cw/2
oy = ch/2

theta1 = np.pi
omega1 = 0.0
theta2 = np.pi+0.01
omega2 = 0.0

#.............................. Variable and parameter vectors
y = [theta1,omega1,theta2,omega2]
params = [l1, l2, m1, m2, g]
#.................................. 
t=[0.0,dt]
#.............................. System of equations
def dfdt(y,t,params):
    theta1, omega1, theta2, omega2 = y
    l1, l2, m1, m2, g = params
    sinD = np.sin(theta1-theta2)
    cosD = np.cos(theta1-theta2)
    sint1 = np.sin(theta1)
    sint2 = np.sin(theta2)
    derivs = [omega1, (m2*g*sint2*cosD-m2*sinD*(l1*omega1**2*cosD+l2*omega2**2)-(m1+m2)*g*sint1)/(l1*(m1+m2*sinD**2)), omega2, ((m1+m2)*(l1*omega1**2*sinD-g*sint2+g*sint1*cosD)+m2*l2*omega2**2*sinD*cosD)/(l2*(m1+m2*sinD**2))]
    return derivs
#.............................. Create root window
root=Tk()
root.title('Double pendulum')
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

#.................................. Main Loop
while RunAll:
    #.................................. Draw oscillator
    canvas.delete(ALL)
    x1 = ox+l1*np.sin(theta1)
    y1 = oy+l1*np.cos(theta1)
    x2 = x1+l2*np.sin(theta2)
    y2 = y1+l2*np.cos(theta2)
    canvas.create_line(ox, oy, x1, y1, fill='black')
    canvas.create_oval(x1-rad,y1-rad,x1+rad,y1+rad,fill='Red')
    canvas.create_line(x1, y1, x2, y2, fill='black')
    canvas.create_oval(x2-rad,y2-rad,x2+rad,y2+rad,fill='Red')
    canvas.update()
    if RunIter:
        psoln=odeint(dfdt,y,t,args=(params,))
        theta1=psoln[1,0]
        omega1=psoln[1,1]
        theta2=psoln[1,2]
        omega2=psoln[1,3]
        #.................................. Update vector
        y=[theta1, omega1, theta2, omega2]
    canvas.after(delay)

root.destroy()