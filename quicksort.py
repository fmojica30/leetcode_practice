#!/usr/bin/env python
# -*- coding: utf-8 -*-

def quickSort(s):
    if (len(s) <= 1):
        return s
    else:
        pivot = s.pop()

    items_greater = []
    items_less = []

    for item in s:
        if item > pivot:
            items_greater.append(item)
        else:
            items_less.append(item)

    return quickSort(items_less) + [pivot] + quickSort(items_greater)

print(quickSort([6,3,45,5,8,423,56,65]))
