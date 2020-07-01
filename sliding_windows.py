#!/usr/bin/env python
# -*- coding: utf-8 -*-
from copy import deepcopy

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        
        current_moves = 0
        self.lowest_moves = -1
        zero_x = None
        zero_y = None
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j]) == 0:
                    zero_x = j
                    zero_y = i
        
        done = []

        self.helper(board, zero_x, zero_y, current_moves)
        return self.lowest_moves
    
    def valid(self, board):
        valid_board = [[1,2,3],[4,5,0]]
        return board == valid_board
    
    def move(self, board, zero_x, zero_y, direction):
        print(direction)
        if direction == "down":
            board[zero_y][zero_x], board[zero_y + 1][zero_x] = board[zero_y + 1][zero_y], board[zero_x][zero_y]
        elif direction == "up":
            board[zero_y][zero_x], board[zero_y - 1][zero_x] = board[zero_y - 1][zero_x], board[zero_x][zero_y]
        elif direction == "right":
            board[zero_y][zero_x], board[zero_y][zero_x + 1] = board[zero_y][zero_x + 1], board[zero_x][zero_y]
        else:
            board[zero_y][zero_x], board[zero_y][zero_x - 1] = board[zero_y][zero_x - 1], board[zero_x][zero_y]
        return board
    
    def helper(self, board, zero_x, zero_y, current_moves):

        if self.valid(board):
            if (self.lowest_moves == -1):
                self.lowest_moves = current_moves
                return
            elif (self.lowest_moves > current_moves):
                self.lowest_moves = current_moves
                return
            else:
                return 
            
        if (zero_x == 1 and zero_y == 2 and not self.valid(board)):
            return 
        
        if (zero_y == 0):
            if (zero_x == 0):
                down_board = deepcopy(board)
                down_board = self.move(down_board, zero_x, zero_y, "down") #down board
                self.helper(board, zero_x, zero_y + 1, current_moves + 1)

                right_board = deepcopy(board)
                right_board = self.move(right_board, zero_x, zero_y, "right") #right board
                self.helper(right_board, zero_x + 1, zero_y, current_moves + 1)
                
            elif (zero_x == 1):
                down_board = deepcopy(board)
                down_board = self.move(down_board, zero_x, zero_y, "down") #down board
                self.helper(board, zero_x, zero_y + 1, current_moves + 1)
                
                right_board = deepcopy(board)
                right_board = self.move(right_board, zero_x, zero_y, "right") #right board
                self.helper(right_board, zero_x + 1, zero_y, current_moves + 1)
                
                left_board = deepcopy(board) 
                left_board = self.move(left_board, zero_x, zero_y, "left") #left board
                self.helper(board, zero_x - 1, zero_y, current_moves + 1)
                
            elif (zero_x == 2):
                down_board = deepcopy(board)
                down_board = self.move(down_board, zero_x, zero_y, "down") #down board
                self.helper(board, zero_x, zero_y + 1, current_moves + 1)

                left_board = deepcopy(board) 
                left_board = self.move(left_board, zero_x, zero_y, "left") #left board
                self.helper(board, zero_x - 1, zero_y, current_moves + 1)

        elif (zero_y == 1):
          
            if (zero_x == 0):
                up_board = deepcopy(board)
                up_board = self.move(up_board, zero_x, zero_y, "up")
                self.helper(up_board, zero_x, zero_y -  1, current_moves + 1)
                
                right_board = deepcopy(board)
                right_board = self.move(right_board, zero_x, zero_y, "right") #right board
                self.helper(right_board, zero_x + 1, zero_y, current_moves + 1)
                
            elif (zero_x == 1):
                up_board = deepcopy(board)
                up_board = self.move(up_board, zero_x, zero_y, "up")
                self.helper(up_board, zero_x, zero_y -  1, current_moves + 1)
                
                right_board = deepcopy(board)
                right_board = self.move(right_board, zero_x, zero_y, "right") #right board
                self.helper(right_board, zero_x + 1, zero_y, current_moves + 1)
                
                left_board = deepcopy(board) 
                left_board = self.move(left_board, zero_x, zero_y, "left") #left board
                self.helper(board, zero_x - 1, zero_y, current_moves + 1)
                
            elif (zero_x == 2):
                up_board = deepcopy(board)
                up_board = self.move(up_board, zero_x, zero_y, "up")
                self.helper(up_board, zero_x, zero_y -  1, current_moves + 1)
                
                left_board = deepcopy(board) 
                left_board = self.move(left_board, zero_x, zero_y, "left") #left board
                self.helper(board, zero_x - 1, zero_y, current_moves + 1)
        
        return 



def main():
    board = [[1, 2, 3], [4, 0, 5]]
    valid_board = [[1,2,3],[4,5,0]]

    x = Solution()
    print(x.slidingPuzzle(board))

main()
