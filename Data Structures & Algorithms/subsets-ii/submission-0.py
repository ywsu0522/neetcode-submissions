class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(i, subset):
            # base case
            if i == len(nums):
                result.append(subset[::])
                return
            
            # nums[i] is chosen
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # nums[i] is not chosen
            while (i + 1 < len(nums)) and (nums[i] == nums[i+1]):
                i += 1

            backtrack(i + 1, subset)

        backtrack(0, [])

        return result

