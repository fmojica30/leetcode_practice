#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def preOrder(root):
    if not root:
        return 

    print(root.value)
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if not root:
        return

    inOrder(root.left)
    print(root.value)
    inOrder(root.right)

def postOrder(root):
    if not root:
        return 

    postOrder(root.left)
    postOrder(root.right)
    print(root.value)

def maxDepth(root, temp):
    if not root:
        return temp

    return max(maxDepth(root.left, temp + 1), maxDepth(root.right, temp + 1))

def maxDepth2(root):
    if not root:
        return 0
    left = maxDepth2(root.left)
    right = maxDepth2(root.right)

    return max(left, right) + 1

def isBalanced(root):
    if not root:
        return True

    left = getHeight(root.left)
    right = getHeight(root.right)

    if abs(left - right) > 1:
        return False

    return isBalanced(root.left) and isBalanced(root.right)

def getHeight(root):
    if not root:
        return 0

    left = getHeight(root.left)
    right = getHeight(root.right)

    return max(left, right) + 1


def main():
    # f = Node(6, None, None)
    e = Node(5, None, None)
    d = Node(4, None, None)
    b = Node(2, e, None)
    c = Node(3, d, None)
    a = Node(1, b, c)
    
    inOrder(a)
    print("---")
    preOrder(a)
    print("---")
    postOrder(a)

    print("--- Max Depth ---")
    print("me :" + str(maxDepth(a, 0)))
    print("Pathrise :" + str(maxDepth2(a)))

    print("--- Is Balanced --")
    print("me : " + str(isBalanced(a)))

main()

