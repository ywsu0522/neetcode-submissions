class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        depth = 0
        N = len(board)
        M = len(board[0])
        record = set()

        def check(i, j, depth, record) -> bool:
            if (i < 0 or i > N - 1 or j < 0 or j > M - 1):
                return False

            if (i, j) in record:
                # 拜訪過，跳過
                return False

            if board[i][j] != word[depth]:
                # 不是我要的，跳過
                return False

            # board[i][j] == word[depth]
            if len(word) == depth + 1:
                return True

            depth += 1
            record.add((i, j))
            if (check(i + 1, j, depth, record) or
                check(i - 1, j, depth, record) or
                check(i, j + 1, depth, record) or
                check(i, j - 1, depth, record)):
                return True
            else:
                record.remove((i, j))
                return False


        for i in range(N):
            for j in range(M):
                if check(i, j, depth, record):
                    return True

        return False

