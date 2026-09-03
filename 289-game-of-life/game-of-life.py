class Solution:
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                count = 0

                for x in range(max(0, i-1), min(m, i+2)):
                    for y in range(max(0, j-1), min(n, j+2)):
                        if (x, y) != (i, j) and abs(board[x][y]) == 1:
                            count += 1

                if board[i][j] == 1 and (count < 2 or count > 3):
                    board[i][j] = -1
                elif board[i][j] == 0 and count == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1