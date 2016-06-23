import time
from tkinter import *
print("Instrucciones para mover las figuras:")
print("Triangulo:\n utilice las flechas de direccion")
print("Rectangulo:\n arriba = w\n abajo = x\n izquierda = a\n derecha = d")
print("Circulo:\n arriba = u\n abajo = n\n izquierda = h\n derecha = k")
time.sleep(10)
tk=Tk()
ventana= Canvas(tk, width=400, height=500)
ventana.pack()
fig=ventana.create_polygon(20,10,20,60,80,35, fill="yellow")
rec=ventana.create_rectangle(20,90, 80, 120, fill="blue")
cir=ventana.create_oval(20, 200, 80, 150, fill="red")

def MovimientoTriangulo(event):
    if event.keysym == 'Up':
        ventana.move(fig,0,-3)
    elif event.keysym == 'Down':
        ventana.move(fig,0,3)
    elif event.keysym == 'Left':
        ventana.move(fig,-3,0)
    elif event.keysym == 'Right':
        ventana.move(fig, 3, 0)
       
def MovimientoRectangulo(event):
    if event.keysym == 'w':
        ventana.move(rec,0,-3)
    elif event.keysym == 'x':
        ventana.move(rec,0,3)
    elif event.keysym == 'a':
        ventana.move(rec,-3,0)
    elif event.keysym == 'd':
        ventana.move(rec, 3, 0)

def MovimientoCirculo(event):
    if event.keysym == 'u':
        ventana.move(cir,0,-3)
    elif event.keysym == 'n':
        ventana.move(cir,0,3)
    elif event.keysym == 'h':
        ventana.move(cir,-3,0)
    elif event.keysym == 'k':
        ventana.move(cir,3,0)

ventana.bind_all('<KeyPress-Up>',MovimientoTriangulo)
ventana.bind_all('<KeyPress-Down>',MovimientoTriangulo)
ventana.bind_all('<KeyPress-Left>',MovimientoTriangulo)
ventana.bind_all('<KeyPress-Right>',MovimientoTriangulo)

ventana.bind_all('<w>',MovimientoRectangulo)
ventana.bind_all('<x>',MovimientoRectangulo)
ventana.bind_all('<a>',MovimientoRectangulo)
ventana.bind_all('<d>',MovimientoRectangulo)

ventana.bind_all('<u>',MovimientoCirculo)
ventana.bind_all('<n>',MovimientoCirculo)
ventana.bind_all('<h>',MovimientoCirculo)
ventana.bind_all('<k>',MovimientoCirculo)
ventana.move(rec,0,3)

tk.mainloop()