import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / (2 ** 0.5))
            t.left(angle)

def pythagoras(t, order, size, angle1, angle2, factor=2 ** 0.5):
    if order == 0:
        t.forward(size)
        t.pu()
        t.back(size)
        # t.right(angle)
        t.pd()
        
    else:
        t.forward(size)
        t.left(angle1)
        pythagoras(t, order - 1, size / factor, angle1, angle2, factor)
        t.right(angle1 + angle2)
        pythagoras(t, order - 1, size / factor, angle1, angle2, factor)
        t.pu()
        t.left(angle2)
        t.back(size)
        t.pd()

        

def draw_tree(order, angle1, angle2, size=200):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(0, -size*1.5)
    t.pendown()
    t.left(90)

    pythagoras(t, order, size, angle1, angle2, 1.414)

    window.mainloop()

if __name__ == '__main__':
# Виклик функції
    level = int(input('Введіть рівень: '))

# Два числа це лівий та правий кут повроту, в класичному випадку, вони обидва 45
    draw_tree(level, 30, 45)