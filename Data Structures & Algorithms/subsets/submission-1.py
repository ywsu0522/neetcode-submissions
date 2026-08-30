class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def search(i, subset):
            if i >= len(nums):
                result.append(subset[:])
                return

            # Choose nums[i]
            subset.append(nums[i])
            search(i + 1, subset)
            subset.pop()

            # Not choose numse[i]
            search(i + 1, subset)

        search(0, [])

        return result