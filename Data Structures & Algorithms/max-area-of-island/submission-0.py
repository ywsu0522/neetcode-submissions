class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        visited = [[False] * M for _ in range(N)]

        def update_status(grid, visited, i, j):
            count = 0
            if grid[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                count += 1
                if i > 0:
                    count += update_status(grid, visited, i - 1, j)
                if i < N - 1:
                    count += update_status(grid, visited, i + 1, j)
                if j > 0:
                    count += update_status(grid, visited, i, j - 1)
                if j < M - 1:
                    count += update_status(grid, visited, i, j + 1)

            return count

        max_count = 0
        for i in range(N):
            for j in range(M):
                count = update_status(grid, visited, i, j)
                if count > max_count:
                    max_count = count
        
        return max_count
