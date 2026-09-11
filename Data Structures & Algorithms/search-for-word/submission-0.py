class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board[0])
        N = len(board)

        def exist_at(i, j, k, explored):
            # k = index of character we're trying to match
            if k == len(word):
                return True

            if (
                i < 0 or i >= N or
                j < 0 or j >= M or
                board[i][j] != word[k] or
                (i, j) in explored
            ):
                return False

            explored.append((i, j))

            found = (
                exist_at(i + 1, j, k + 1, explored) or
                exist_at(i - 1, j, k + 1, explored) or
                exist_at(i, j + 1, k + 1, explored) or
                exist_at(i, j - 1, k + 1, explored)
            )

            explored.pop()

            return found

        for i in range(N):
            for j in range(M):
                if exist_at(i, j, 0, []):
                    return True

        return False
