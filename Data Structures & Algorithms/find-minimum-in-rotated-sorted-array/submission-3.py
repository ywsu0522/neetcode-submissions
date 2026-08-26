class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        # [lo, hi]
        while (lo < hi):
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                # Otherwise lo == hi makes infty loop
                hi = mid

        return nums[lo]