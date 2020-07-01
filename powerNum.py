#!/usr/bin/env python
# -*- coding: utf-8 -*-

def powerNumber(base, exp):

    if (exp == 0):
        return 1
    else:
        ans = base
        for i in range(exp):
           ans *= base

    return ans


def main():

    print(powerNumber(2,0))
    print(powerNumber(3,3))


main()
