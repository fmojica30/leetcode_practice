#!/usr/bin/env python
# -*- coding: utf-8 -*-
from copy import deepcopy

class Queue(object):
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
        return

    def dequeue(self):
        return self.queue.pop(0)

        
class Solution():
    def slidingPuzzles(self, board):
        valid_puzzle = [[1,2,3],[4,5,0]]
        todo = Queue()
        done = []
        x = None
        y = None
        num_moves = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] == 0):
                    x = i
                    y = j
        xMoves = [1,-1,0,0]
        yMoves = [0,0,1,-1]
        todo.enqueue(board)

        while len(todo.queue > 0):
            check = todo.dequeue()
            if check == valid_puzzle:
                return True

            for i in range(4):
                new_x = x + xMoves[i]
                new_y = y + yMoves[i]
                
                if (self.valid_move(new_x, new_y)):
                    moved = deepcopy(check)
                    moved[y][x], moved[new_y][new_x] = moved[new_y][new_x], moved[y][x]
                    todo.enqueue(moved)
        return -1
    
    def valid_move(self, x, y):
        return (x <= 2 and x >= 0 and y <= 1 and y >= 0)

def main():
    x = Solution()
    
main()
