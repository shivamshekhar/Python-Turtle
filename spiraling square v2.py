from turtle import Turtle
t = Turtle()

def polygon(n,theta):
    t.speed(0)
    t.right(theta)
    a = (180*(n-2))/n
    for x in range(n):
        t.forward(100)
        t.right(180 - a)

for i in range(180):
    polygon(4,i)
input('Press any key to continue...')
