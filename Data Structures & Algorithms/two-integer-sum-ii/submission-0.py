class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1
        while (lo < hi) and (numbers[lo] + numbers[hi] != target):
            if numbers[lo] + numbers[hi] > target:
                hi -= 1
            else:
                lo += 1

        return [lo + 1, hi + 1]