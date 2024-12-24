import turtle
import time

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("pink")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def draw_heart(x, y, size, color, thickness):
    t.penup()
    t.goto(x, y)
    t.color(color)
    t.pensize(thickness)
    t.pendown()
    t.begin_fill()
    t.left(140)
    t.forward(size)

    for _ in range(200):
        t.right(1)
        t.forward(size * 0.009)

    t.left(120)

    for _ in range(200):
        t.right(1)
        t.forward(size * 0.009)
    
    t.forward(size)
    t.end_fill()
    t.setheading(0)

hearts = [
    (0, -150, 300, "#FF9999", 5),
    (0, -135, 270, "#FFCCCC", 5),
    (0, -120, 240, "#FFE6E6", 5),
    (0, -105, 210, "#FFCCCC", 5),
    (0, -90, 180, "#FF99CC",5),
    (0, -75, 150, "#FFCCFF", 5),
    (0, -50, 100, "#0CBCCC", 5)
]

for heart in hearts:
    x, y, size, color, thickness = heart
    draw_heart(x, y, size, color, thickness)
    time.sleep(0.5)  # Añade un retraso de 0.5 segundos entre cada corazón

# Añadir texto en el centro del corazón más grande
t.penup()
t.goto(0, -200)
t.color("Blue")
t.write("Te amo mi princesita", align="center", font=("Arial", 24, "bold"))

screen.mainloop()