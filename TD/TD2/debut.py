import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

tk.root = tk.Tk()

tk.canvas = tk.Canvas(tk.root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x = CANVAS_WIDTH/2
y0 = 60
y1 = CANVAS_HEIGHT - 60
tk.canvas.create_line(x, y0, x, y1)
tk.canvas.create_oval(x+50, y0 - 50, x-50 , y0 + 50)
tk.canvas.create_oval(x+50, y1 - 50, x-50 , y1 + 50)
tk.canvas.create_oval(x+50, (y0 + y1) / 2 - 50, x-50, (y0 + y1) / 2 + 50)
    
# Fin de votre code

tk.canvas.grid(row=0,column=0)
tk.root.mainloop()
