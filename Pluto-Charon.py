import numpy as np
from tkinter import *
from scipy.integrate import odeint
#.....................................................
root=Tk()
root.title('Pluto-Charon system')
#..................................................... Open canvas
cw=ch=800
canvas=Canvas(root,width=cw,height=ch,background='black')
canvas.grid(row=0,column=0)
#.....................................................
Ox=Oy=cw/2
#..................................................... Pluto
m1=1.3e22
x1=y1=0
vx1=vy1=0
rad1=20
#..................................................... Charon
m2=1.6e21
x2=1.9e7
y2=0
vx2=0
vy2=2e2
rad2=10
#..................................................... Gravitational constant
G=6.67408e-11
#..................................................... 
dt=600
delay=1
scale=2e-5
#..................................................... move to barycenter system
mtot=m1+m2
xb=(m1*x1+m2*x2)/mtot
yb=(m1*y1+m2*y2)/mtot
vxb=0
vyb=(m1*vy1+m2*vy2)/mtot
x1-=xb
y1-=yb
vx1-=vxb
vy1-=vyb
x2-=xb
y2-=yb
vx2-=vxb
vy2-=vyb
#..................................................... Initial conditions
y=[x1,y1,vx1,vy1,x2,y2,vx2,vy2]
t=[0.0,dt]
#..................................................... function
def dfdt(yInp,t):
    global G
    x1,y1,vx1,vy1,x2,y2,vx2,vy2=yInp
    distx=x2-x1
    disty=y2-y1
    r2=distx**2+disty**2
    alpha=np.arctan2(disty,distx)
    f=G/r2
    fx=f*np.cos(alpha)
    fy=f*np.sin(alpha)
    ax1=fx*m2
    ay1=fy*m2
    ax2=-fx*m1
    ay2=-fy*m1
    return [vx1,vy1,ax1,ay1,vx2,vy2,ax2,ay2]
line=[Ox+x2*scale,Oy-y2*scale]
while True:
    canvas.delete(ALL)
    canvas.create_line(0,Oy,cw,Oy,fill='white')
    canvas.create_line(Ox,0,Ox,ch,fill='white')
    canvas.create_oval(Ox+x1*scale-rad1,Oy-y1*scale-rad1,Ox+x1*scale+rad1,Oy-y1*scale+rad1,fill='yellow')
    canvas.create_oval(Ox+x2*scale-rad2,Oy-y2*scale-rad2,Ox+x2*scale+rad2,Oy-y2*scale+rad2,fill='blue')
    line.append(Ox+x2*scale)
    line.append(Oy-y2*scale)
    canvas.create_line(line,fill='red')
    canvas.update()
    #.....................................................
    psoln=odeint(dfdt,y,t)
    y=psoln[1,:]
    x1,y1,vx1,vy1,x2,y2,vx2,vy2=y
    canvas.after(delay)