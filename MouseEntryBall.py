from tkinter import *
#.....................................................Global Variables
RunAll=True
RunMotion=GetData=Grabbed=False
#.....................................................Start/Stop Motion
def StartStop():
    global RunMotion
    RunMotion=not RunMotion
    if RunMotion:
        StartButton['text']='Stop'
    else:
        StartButton['text']='Restart'
#.....................................................Exit the program
def StopAll():
    global RunAll
    RunAll=False
#.....................................................Read entries
def ReadData(*arg):
    global GetData
    GetData=True
#.....................................................Grab ball
def GrabBall(event):
    global Grabbed,rad,RunMotion,x,y
    if not RunMotion:
        Grabbed=((x-event.x)**2+(y-event.y)**2)<rad**2
#.....................................................Release ball
def ReleaseBall(event):
    global Grabbed
    Grabbed=False
#.....................................................Drag Ball
def DragBall(event):
    global Grabbed,x,y
    if Grabbed:
        x,y=event.x,event.y

#.....................................................Create a root window
root=Tk()
root.title('Entry ball')
root.bind('<Return>',ReadData)
#.....................................................Add canvas to the root window
cw=800
ch=400
canvas=Canvas(root,width=cw,height=ch,background='white')
canvas.grid(row=0,column=0)
#.....................................................Mouse button
canvas.bind('<Button-1>',GrabBall)
canvas.bind('B1-Motion',DragBall)
canvas.bind('ButtonRelease-1',ReleaseBall)
#.....................................................Add toolbar to rootwindow
toolbar=Frame(root)
toolbar.grid(row=0,column=1,sticky=N)
#.....................................................Toolbar buttons
StartButton=Button(toolbar,text="Start",command=StartStop,width=7)
StartButton.grid(row=0,column=0)
CloseButton=Button(toolbar,text='Close',command=StopAll)
CloseButton.grid(row=0,column=1)
#.....................................................Toolbar labels and entries
LabVx=Label(toolbar,text='Vx')
LabVx.grid(row=1,column=0)
EntryVx=Entry(toolbar,bd=5,width=8)
EntryVx.grid(row=1,column=1)
LabelAccel=Label(toolbar,text='Ay')
LabelAccel.grid(row=2,column=0)
EntryAccel=Entry(toolbar,bd=5,width=8)
EntryAccel.grid(row=2,column=1)
#.....................................................Variables
delay=20 #milliseconds
rad=20
color='red'
x=rad
y=ch-rad
vx=4.0
vy=-7.5
ay=0.1
#.....................................................Write variable values into entries
EntryVx.insert(0,'{:.2f}'.format(vx))
EntryAccel.insert(0,'{:.2f}'.format(ay))
#.....................................................Main loop
while RunAll:
    #.....................................................Draw ball on canvas
    canvas.delete(ALL)
    canvas.create_oval(x-rad,y-rad,x+rad,y+rad,fill=color)
    canvas.update()
    #.....................................................Ball is moving
    if RunMotion:
        #.....................................................Bouncing
        if (x+rad)>=cw:
            vx=-abs(vx)
        elif (y+rad)>=ch:
            vy=-abs(vy)
        elif x<=rad:
            vx=abs(vx)
        elif y<=rad:
            vy=abs(vy)
        #.....................................................Update position and velocity
        x+=vx
        y+=vy+0.5*ay
        vy+=ay
    #.....................................................Read entries
    elif GetData:
        try:
            vx=float(EntryVx.get())
        except:
            pass
        try:
            ay=float(EntryAccel.get())
        except ValueError:
            pass
        EntryVx.delete(0,'end')
        EntryVx.insert(0,'{:.2f}'.format(vx))
        EntryAccel.delete(0,'end')
        EntryAccel.insert(0,'{:.2f}'.format(ay))
        GetData=False
    #.....................................................Wait delay time
    canvas.after(delay)
    #.....................................................
root.destroy()
