# Turtle Artist
# Author:
# 28 October

import random
import turtle

from functools import cache

# A one-of-a-kind drawing

wn = turtle.Screen()
t = turtle.Turtle()

# Draw a house
def draw_house(x: int, y:int):
    """Draws a house using turtle at given coords

    x - center-x of the house
    y - center-y of the house"""
    # Draw the outline
    # Draw the roof
    # Draw the windows
    # Draw the door
    # Draw the chimney

def recursive_fun(level: int, dir: str):
    if dir == "left" and level > 0:
        # some code
        recursive_fun(level - 1, "right")
        print("right!")
    elif dir == "right" and level > 0:
        recursive_fun(level - 1, "left")
        print("left!")

@cache
def fib(num: int) -> int:
    if num > 2:
        return fib(num - 1) + fib(num - 2)
    else:
        return 1


def snowflake(level: int, length: float):
    if level > 0:
        for _ in range(7):
            t.forward(length)
            snowflake(level - 1, length * .3)
            t.backward(length)
            t.left(360 / 7)


# print(fib(1000))
# print(fib(1))
# print(fib(2))
# print(fib(3))

# recursive_fun(9, "left")

t.speed(0)
t.pd()
snowflake(3, 200)

wn.exitonclick() # last line of code
