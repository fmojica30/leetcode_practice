import copy


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        self.queue.pop(0)
        return

    def peek(self):
        return self.queue[0]


class BoardInfo():
    def __init__(self, board, x, y, moves):
        self.board = board
        self.x = x
        self.y = y
        self.moves = moves

    def __str__(self):
        return str(self.board)


class Solution():
    def sliding_puzzle(self, board):
        self.lowest_move = -1
        x = None
        y = None
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] == 0):
                    x = i
                    y = j

        todo = Queue()
        todo.enqueue(BoardInfo(board, x, y, 0))
        done = []

        self.helper(todo, done)

        return self.lowest_move

    def helper(self, todo, done):
        if (len(todo.queue) == 0):
            return

        moves_x = [1, -1, 0, 0]
        moves_y = [0, 0, 1, -1]

        while (len(todo.queue) > 0):
            check = todo.peek()
            if (self.valid_board(check.board)):
                self.lowest_move = check.moves
                break

            elif (check.board in done):
                todo.dequeue()
                continue

            else:
                for i in range(4):
                    new_x = check.x + moves_x[i]
                    new_y = check.y + moves_y[i]

                    if (self.valid_move(new_x, new_y)):

                        new_move_board = self.swap(
                            check.x, check.y, new_x, new_y, check.board)
                        board_info = BoardInfo(
                            new_move_board, new_x, new_y, check.moves + 1)
                        todo.enqueue(board_info)

                done.append(check.board)

            todo.dequeue()

        return

    def valid_board(self, board):
        return board == [[1, 2, 3], [4, 5, 0]]

    def valid_move(self, x, y):
        return (x <= 1 and x >= 0 and y <= 2 and y >= 0)

    def swap(self, x, y, new_x, new_y, board):
        new_board = copy.deepcopy(board)
        new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
        return new_board


def main():
    a = Solution()
    board = [[3, 2, 4], [1, 5, 0]]
    print(a.sliding_puzzle(board))
    #check = a.swap(1,1,0,1, board)
    # print("***")
    # for i in range(2):
    #    print(check[i])
    # print("---")
    # for i in range(2):
    #    print(board[i])
    # print("***")


main()
