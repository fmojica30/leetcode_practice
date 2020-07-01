#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class Thing(object):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.color

def sortByColor(arr):
    pivot = arr.pop()
    
    color1 = []
    color2 = []
    color3 = []

    for thing in arr:
        if (thing.color == "red"):
            color1.append(thing.color)
        elif (thing.color == "blue"):
            color2.append(thing.color)
        else:
            color3.append(thing.color)

    return color1 + color2 + color3

def main():
    arrTest = []
    colors = ["red", "blue", "white"]

    for i in range(9):
        color = random.randint(0, 2)
        x = Thing(colors[color])
        arrTest.append(x)

    print(sortByColor(arrTest))

main()
