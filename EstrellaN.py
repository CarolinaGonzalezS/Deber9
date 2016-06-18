import turtle
import os
n=int(input("ingrese el numero de puntas impares:\n"))
t1=turtle.Screen()
t1.bgcolor("blue")
t=turtle.Pen()
ang=180/n
ang1=180-ang    
t.left(ang)
for x in range(1,n+1):
    t.color(1,0,0)
    t.begin_fill()    
    t.left(ang1)
    t.forward(200)
    
t.end_fill()
    

turtle.getscreen()._root.mainloop()