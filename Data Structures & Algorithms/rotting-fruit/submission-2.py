class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh_cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_cnt += 1
                if grid[i][j] == 2:
                    queue.append((i, j))

        minute = 0
        N = len(grid)
        M = len(grid[0])
        while queue and (fresh_cnt > 0):
            qsize = len(queue)
            for _ in range(qsize):
                i, j = queue.popleft()
                if i > 0:
                    if grid[i - 1][j] == 1:
                        grid[i - 1][j] = 2
                        queue.append((i - 1, j))
                        fresh_cnt -= 1
                if i < N - 1:
                    if grid[i + 1][j] == 1:
                        grid[i + 1][j] = 2
                        queue.append((i + 1, j))
                        fresh_cnt -= 1
                if j > 0:
                    if grid[i][j - 1] == 1:
                        grid[i][j - 1] = 2
                        queue.append((i, j - 1))
                        fresh_cnt -= 1
                if j < M - 1:
                    if grid[i][j + 1] == 1:
                        grid[i][j + 1] = 2
                        queue.append((i, j + 1))
                        fresh_cnt -= 1

            minute += 1

        if fresh_cnt > 0:
            return -1

        return minute
