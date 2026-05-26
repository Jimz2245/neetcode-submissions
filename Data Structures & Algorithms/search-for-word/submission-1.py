class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])

        def find(row, col, i):
            if i == len(word):
                return True
            if row>=r or row<0 or col>=c or col<0 or board[row][col] != word[i] or board[row][col] == '#':
                return False
            board[row][col] = '#'
            res = (find(row+1, col, i+1) or
                    find(row-1, col, i+1) or
                    find(row, col+1, i+1) or
                    find(row, col-1, i+1))
            board[row][col] = word[i]
            return res
        for i in range(r):
            for j in range(c):
                if find(i, j, 0) == True:
                    return True
        return False