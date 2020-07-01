#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/bin/python3

#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY puzzle as parameter.

# Info is used to keep track of the moves used when going through the combinations
class BoardInfo():
    def __init__(self, board, x, y, moves):
        self.board = board
        self.x = x
        self.y = y
        self.moves = moves

#Queue will be used to keep track of the moves we have to check in order so we get the lowest
#number of moves
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

#this function checks to see if the move made is valid and stays on the board
def valid_move(x, y, m, n):
    return (x >= 0 and x < m and y >= 0 and y < n)

#does the move and returns a different board with the move made
def swap(board, x, y, new_x, new_y, n):
    new_board = decode(board, n)
    new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
    encoded_board = encode(new_board)
    return encoded_board

# Encode and decode are to make the lookup time faster in the already done array
def encode(board):
    string = ""
    for i in range(len(board)):
        for j in range(len(board[i])):
            string += str(board[i][j])
    return string

def decode(string, n):
    board = []
    row = []
    for i in range(len(string)):
        row.append(int(string[i]))
        if (len(row) == n):
            board.append(row)
            row = []
    return board

def movesToSolve(puzzle):
    # Write your code here
    #initializing coordinates of the 0
    x = None
    y = None

    # Finding out length and width of the board
    m = len(puzzle)
    n = len(puzzle[0])

    # making the solved board to check against the moves we make
    solved = ""
    for i in range(m * n):
        solved += str(i)

    # finding the initial position of the 0
    for i in range(m):
        for j in range(n):
            if (puzzle[i][j] == 0):
                x = i
                y = j

    # These moves are possible moves that the 0 can make up left down or right
    # Moves are made by taking combinations from both arrays 
    moves_x = [1, -1, 0, 0]
    moves_y = [0, 0, 1, -1]

    # Queue that has the ones we have to do next
    todo = Queue()
    
    # array that holds all the ones we have done so that we dont check it twice
    done = []

    initial_board = BoardInfo(encode(puzzle), x, y, 0)

    todo.enqueue(initial_board)

    #This while loop goes until the queue is empty at which point all the possible moves are        checked

    while len(todo.queue) > 0:
        check = todo.peek()
        if (check.board == solved):
            return check.moves

        # This check is in case the board were looking at we already checked
        elif (check.board in done):
            todo.dequeue()
            continue

        else:
            """
            Inner for loop uses the moves arrays to change the x and y of the 0
            in every possible direction and uses the ones that are valid moves to make
            new boards
            """
            for i in range(4):
                new_x = check.x + moves_x[i]
                new_y = check.y + moves_y[i]

                if (valid_move(new_x, new_y, m, n)):
                    new_move_board = swap(check.board, check.x, check.y, new_x, new_y, n)
                    new_info = BoardInfo(new_move_board, new_x, new_y, check.moves + 1)
                    todo.enqueue(new_info)
            
            done.append(check.board)

        todo.dequeue()
    
    return -1

def main():
    puzzle = [[2,7,1], [6,3,5], [0,4,8]]
    print(movesToSolve(puzzle))

main()










