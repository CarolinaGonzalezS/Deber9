import time
from tkinter import *
tk=Tk()
ventana= Canvas(tk, width=400, height=500)
ventana.pack()
fig=ventana.create_polygon(20,10,20,60,80,35, fill="yellow")
rec=ventana.create_rectangle(20,90, 80, 120, fill="blue")
cir=ventana.create_oval(20, 200, 80, 150, fill="red")

for x in range(0,60):
	ventana.move(fig, 5,0 )	
	ventana.move(rec, 5,0 )	
	ventana.move(cir, 5,0 )	
	tk.update()
	time.sleep(0.05)

tk.mainloop()