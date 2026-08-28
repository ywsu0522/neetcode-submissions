class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(subset, n_open, n_close):
            if n_open == n_close and n_open == n:
                result.append(subset[:])
                return

            # n_open > n_close or n_open < n
            if n_open < n:
                subset += '('
                backtrack(subset, n_open + 1, n_close)
                subset = subset[:-1]

            if n_open > n_close:
                subset += ')'
                backtrack(subset, n_open, n_close + 1)

        backtrack("", 0, 0)

        return result
