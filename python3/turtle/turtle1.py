from turtle import *
n=400
color('red', 'yellow')
#begin_fill()

for j in range(4):
    right(60)
    for i in range(3):
        forward(n)
        right(120)
    n=n/2
    forward(n)
