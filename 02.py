import turtle
import sys


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snow(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    # Draw curve, rotate turtle, draw, rotate, draw
    koch_curve(t, order, size)
    t.right(120)
    koch_curve(t, order, size)
    t.right(120)
    koch_curve(t, order, size)

    window.mainloop()


def main():
    # Turtle does not work on Python > 3.8 on Mac
    if (sys.version_info[0] >= 3) and (sys.version_info[1] > 8):
        print("Use Python 3.x < 3.9")
        exit()
    # Waiting integer number input
    while True:
        try:
            steps = int(input("Set Koch steps >>>"))
            break
        except ValueError:
            print("Please type number!")
    draw_koch_snow(steps)


if __name__ == "__main__":
    main()
