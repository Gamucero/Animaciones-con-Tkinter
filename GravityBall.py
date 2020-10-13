from tkinter import Tk,Canvas,ALL

root=Tk()
root.title('Framed Ball')

cw=600
ch=320

canvas=Canvas(root,width=cw,height=ch,background='white')
canvas.grid(row=0,column=0)

delay=30
rad=5
color='red'
x=rad
y=ch-rad
vx=4.0
vy=-5.0
ay=0.05
line=[x,y]
while True:
    canvas.delete(ALL)
    canvas.create_oval(x-rad,y-rad,x+rad,y+rad,fill=color)
    line.append(x)
    line.append(y)
    canvas.create_line(line,fill='blue')
    canvas.update()
    if (x+rad)>=cw:
        vx=-abs(vx)
    elif (y+rad)>=ch:
        vy=-abs(vy)
    elif x<=rad:
        vx=abs(vx)
    elif y<=rad:
        vy=abs(vy)
    x+=vx
    y+=vy+0.5*ay
    vy+=ay
    canvas.after(delay)