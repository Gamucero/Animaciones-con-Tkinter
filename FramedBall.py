from tkinter import Tk,Canvas,ALL

root=Tk()
root.title('Framed Ball')

cw=800
ch=640

canvas=Canvas(root,width=cw,height=ch,background='white')
canvas.grid(row=0,column=0)

delay=10
rad=40
color='red'
x=rad
y=ch-rad
vx=4.0
vy=-5.0
while True:
    canvas.delete(ALL)
    canvas.create_oval(x-rad,y-rad,x+rad,y+rad,fill=color)
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
    y+=vy
    canvas.after(delay)