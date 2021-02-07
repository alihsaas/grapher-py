import tkinter as Tk
import math
from Equation import Expression

cell_size = 25

def create_grid(event=None):
    w = c.winfo_width() - 2
    h = c.winfo_height() - 2
    c.delete('grid_line')

    for i in range(0, w, cell_size):
        is_center = i == w/2
        if not is_center:
            c.create_rectangle(
                (
                    (i, h/2 - 5),
                    (i, h/2 + 5)
                ),
                width=5
            )
            c.create_text((i, h/2 + cell_size), text=str(i - 500))
        width = 2 if is_center else 1
        c.create_line([(i, 0), (i, h)], tag='grid_line', width=width)

    for i in range(0, h, cell_size):
        is_center = i == h/2
        if not is_center:
            c.create_rectangle(
                (
                    (w/2 - 5, i),
                    (w/2 + 5, i)
                ),
                width=5
            )
            c.create_text((w/2 + cell_size, i), text=str(-i + 500))
        width = 2 if is_center else 1
        c.create_line([(0, i), (w, i)], tag='grid_line', width=width)

def on_changed(sv: Tk.StringVar):
    c.delete("curve")

    w = c.winfo_width()
    h = c.winfo_height()

    inverse_scale_x = 1 / cell_size

    fn = Expression(sv.get(), "x")
    i = 0
    while i <= w:
        x_value = i * inverse_scale_x
        y_value = fn(x_value)
        y_position = h - y_value * cell_size
        print(x_value, y_value)
        print(i, y_position)
        print("-" * 10)
        c.create_oval([
            (i - 1, y_position - 1),
            (i + 1, y_position + 1)
        ], tag="curve")
        i += 0.1


root = Tk.Tk()

Tk.Button(root, text="Quit", command=root.destroy).pack()

expressionHolder = Tk.StringVar()
entry1 = Tk.Entry(root, textvariable=expressionHolder)

entry1.pack()
expressionHolder.trace("w", lambda name, index, mode, sv=expressionHolder: on_changed(sv))

c = Tk.Canvas(root, height=1000, width=1000, bg='white')
c.pack(fill=Tk.BOTH, expand=True)

c.bind('<Configure>', create_grid)


root.mainloop()

