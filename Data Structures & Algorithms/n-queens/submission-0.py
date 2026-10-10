class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def editBoard(results, board: List[List[str]], depth: int):
            if depth == n:
                ret = []
                for i in range(n):
                    str_i = board[i][0]
                    for j in range(1, n):
                        str_i += board[i][j]
                    ret.append(str_i)
                results.append(ret)
                return

            for j in range(n):
                available = True
                for i in range(depth):
                    if board[i][j] == "Q":
                        available = False
                        break
                    
                i = depth - 1
                k = j - 1
                while i >= 0 and k >= 0:
                    if board[i][k] == "Q":
                        available = False
                        break
                    else:
                        i -= 1
                        k -= 1

                i = depth - 1
                k = j + 1
                while i >= 0 and k < n:
                    if board[i][k] == "Q":
                        available = False
                        break
                    else:
                        i -= 1
                        k += 1
                    
                if available:
                    board[depth][j] = "Q"
                    editBoard(results, board, depth + 1)
                    board[depth][j] = "."


        results = []
        board = []
        for i in range(n):
            board.append(["."] * n)
        
        editBoard(results, board, 0)

        return results
