import time
from tkinter import *
tk=Tk()
ventana= Canvas(tk, width=400, height=500)
ventana.pack()
fig=ventana.create_polygon(20,10,20,60,80,35, fill="yellow")
rec=ventana.create_rectangle(20,90, 80, 120, fill="blue")
cir=ventana.create_oval(20, 200, 80, 150, fill="red")

def Movimiento(event):
    if event.keysym == 'Up':
        ventana.move(fig,0,-3)
        ventana.move(rec,0,-3)
        ventana.move(cir,0,-3)
    elif event.keysym == 'Down':
        ventana.move(fig,0,3)
        ventana.move(rec,0,3)
        ventana.move(cir,0,3)
    elif event.keysym == 'Left':
        ventana.move(fig,-3,0)
        ventana.move(rec,-3,0)
        ventana.move(cir,-3,0)
    else:
        ventana.move(fig, 3, 0)
        ventana.move(rec, 3, 0)
        ventana.move(cir,3,0)
       


ventana.bind_all('<KeyPress-Up>',Movimiento)
ventana.bind_all('<KeyPress-Down>',Movimiento)
ventana.bind_all('<KeyPress-Left>',Movimiento)
ventana.bind_all('<KeyPress-Right>',Movimiento)
ventana.move(rec,0,3)

tk.mainloop()