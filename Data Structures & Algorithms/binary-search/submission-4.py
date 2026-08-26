class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        # [lo, hi)

        while (lo < hi):
            # while [lo, hi) nonempty
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1

        return -1

