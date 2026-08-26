class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        # [lo, hi]

        last = nums[-1]
        while (lo <= hi):
            mid = (lo + hi) // 2
            if nums[mid] > last:
                lo = mid + 1
            else:
                # Otherwise lo == hi makes infty loop
                hi = mid - 1

        return nums[lo]