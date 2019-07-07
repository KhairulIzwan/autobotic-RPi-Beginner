#!/usr/bin/env python

import turtle

t = turtle.Turtle()
disp = turtle.Screen()

t.color("black", "yellow")

t.begin_fill()
while True:
	t.forward(100)
	t.left(190)
	print(t.pos())
	if abs(t.pos()) < 1:
		break
t.end_fill()
disp.exitonclick()
