#!/usr/bin/env python
# -*- coding: utf-8 -*-

def binarySearch(arr, target):
    l, r = 0, (len(arr) - 1)
    while l + 1 < r:
        mid = (l + r) // 2
        if (arr[mid] > target):
            r = mid
        elif (arr[mid] < target):
            l = mid
        else:
            return mid
    return -1

def main():
    print(binarySearch([1,2,3,4,5,6,7,8], 5))

main()

