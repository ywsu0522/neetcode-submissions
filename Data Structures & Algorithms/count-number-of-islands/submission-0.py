class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        N = len(grid)
        M = len(grid[0])
        def dfs(i, j, visited):
            if grid[i][j] == "0":
                return
            if visited[i][j]:
                return
            if grid[i][j] == "1":
                visited[i][j] = True

            # 我忘記擋掉 visited node
            if i > 0:
                dfs(i - 1, j, visited)
            if i < N - 1:
                dfs(i + 1, j, visited)
            if j > 0:
                dfs(i, j - 1, visited)
            if j < M - 1:
                dfs(i, j + 1, visited)

        count = 0
        visited = [[False] * M for i in range(N)]
        for i in range(N):
            for j in range(M):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j, visited)
                    count += 1

        return count