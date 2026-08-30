class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def search(i, subset):
            if i >= len(nums):
                result.append(subset[:])
                return

            # Choose nums[i]
            subset_copy = subset[:]
            subset_copy.append(nums[i])
            search(i + 1, subset_copy)

            # Not choose numse[i]
            search(i + 1, subset)

        search(0, [])

        return result