#!/usr/bin/env python
# -*- coding: utf-8 -*-

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return factorial(n-1) * n

def bunnyEars1(n, total = 0):
    if (n == 0):
        return total
    else:
        return bunnyEars1(n - 1, total + 2)

def bunnyEars2(n, total = 0):
    if (n == 0):
        return total 
    elif (n % 2 == 0):
        return bunnyEars2(n - 1, total + 2)
    else:
        return bunnyEars2(n - 1, total + 3)
    
def triangle(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return (1 + 2*n - 2) + triangle(n - 1)

def sumDigits(n):
    if (n % 10 == n):
        return n
    else:
        return (n % 10) + sumDigits(n // 10)

def count7(n):
    if (n % 10 == n):
        if (n == 7):
            return 1
        else:
            return 0
    else:
        if (n % 10 == 7):
            return 1 + count7(n // 10)
        else:
            return count7(n // 10)

def count8(n):
    if (n % 10 == n):
        if (n == 8):
            return 1
        else:
            return 0
    else:
        if (n % 10 == 8):
            if (n % 100 == 88):
                return 2 + count8(n // 10)
            else:
                return 1 + count8(n // 10)
        else:
            return count8(n // 10)

def powerN(base, n):
    if (n == 1):
        return base
    else:
        return base * powerN(base, n - 1)

def countX(s):
    if (len(s) == 1):
        if (s == "x"):
            return 1
        else:
            return 0
    else:
        check = s[len(s) - 1]
        newWord = s[:len(s) -1]

        if (check == "x"):
            return 1 + countX(newWord)
        else:
            return countX(newWord)

def countHi(s):
    if (len(s) == 2 or len(s) == 1):
        if (s == "hi"):
            return 1
        else:
            return 0
    else:
        check = s[len(s) - 2:]
        if (check == "hi"):
            newWord = s[:len(s) - 2]
            return 1 + countHi(newWord)
        else:
            newWord = s[:len(s) - 1]
            return countHi(newWord)



def main():
    print(factorial(9))
    print(bunnyEars2(6))
    print(bunnyEars1(6))
    print(triangle(5))
    print(sumDigits(1234567))
    print(count7(9183724092837509283745))
    print(count8(882838281882))
    print(powerN(3,3))
    print(countX("xavierxentxexexores"))
    print("Count hi: " + str(countHi("slkdjfhihis;lkdjfhilsdkjfjhij")))

main()
