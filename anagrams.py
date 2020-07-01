#!/usr/bin/env python
# -*- coding: utf-8 -*-

def anagrams(a, b):
    if (len(a) != len(b)):
        return False

    aList = {}
    bList = {}
    for letter in a:
        if letter in aList:
            aList[letter] += 1
        else:
            aList[letter] = 1

    for letter in b:
        if letter in bList:
            bList[letter] += 1
        else:
            bList[letter] = 1

    for letter in aList:
        if not (letter in bList and aList[letter] == bList[letter]):
            return False

    return True

def reverse(a, b):
    if (len(a) != len(b)):
        return False

    newStr = ""
    for letter in a:
        newStr = letter + newStr
    print(newStr)
    if (newStr == b):
        return True

    return False

def main():
    print(anagrams("anagrams", "anal"))
    print("---reverse---")
    print(reverse("racecar", "racecar"))
    print(reverse("uilsinojt", "asdkjfhss"))

main()
            
