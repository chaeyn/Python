import turtle
import random
import time
import threading

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("💀 홍준기 핵폭발 시뮬레이터 💥")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

colors = ["#ff0000", "#ff6600", "#ffff00", "#ffffff", "#ff9933", "#ff3300", "#ffcc00"]

def go_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def flash_world():
    for _ in range(40):
        screen.bgcolor(random.choice(colors))
        time.sleep(0.015)  # 원래 0.03 → 절반으로

    screen.bgcolor("black")

def nuclear_ring(x, y):
    go_to(x, y)
    for r in range(10, 300, 5):
        t.color(random.choice(colors))
        t.pensize(2)
        t.circle(r)
        t.right(15)
        time.sleep(0.005)  # 원래 0.01 → 절반

def mushroom_cloud():
    t.color("red")
    go_to(0, -100)
    t.begin_fill()
    t.circle(120)
    t.end_fill()
    t.color("orange")
    go_to(0, 50)
    t.begin_fill()
    t.circle(80)
    t.end_fill()
    t.color("yellow")
    go_to(0, 150)
    t.begin_fill()
    t.circle(40)
    t.end_fill()

def shockwave_lines():
    t.pensize(1)
    for _ in range(100):
        t.color(random.choice(colors))
        go_to(0, 0)
        angle = random.randint(0, 360)
        t.setheading(angle)
        t.forward(300)
        time.sleep(0.0025)  # 원래 0.005 → 절반

def write_finale():
    go_to(-280, -250)
    t.color("white")
    t.write("💀 지구는 사라졌습니다. 홍준기 감성으로요. - THE END", font=("Courier", 16, "bold"))

def countdown():
    go_to(-50, 0)
    t.color("white")
    for i in range(5, 0, -1):
        t.clear()
        t.write(f"{i}", font=("Arial", 48, "bold"))
        time.sleep(0.5)  # 원래 1초 → 절반
    t.clear()
    t.write("💥", font=("Arial", 72, "bold"))
    time.sleep(0.25)  # 원래 0.5초 → 절반
    t.clear()

def execute_the_end():
    countdown()
    flash_world()
    nuclear_ring(0, 0)
    shockwave_lines()
    mushroom_cloud()
    write_finale()

execute_the_end()
turtle.done()