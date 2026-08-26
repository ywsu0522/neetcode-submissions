class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        while (lo <= hi):
            mid = (lo + hi) // 2
            if mid == hi:
                # Only when lo = mid = hi
                return nums[mid]
                
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid