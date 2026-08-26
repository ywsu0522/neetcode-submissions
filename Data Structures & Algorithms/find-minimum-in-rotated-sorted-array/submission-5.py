class Solution:
    def findMin(self, nums: List[int]) -> int:
        # head = nums[0]: If nums[mid] > head: lo = mid + 1
        # possible: head = min_idx, so return lo % N

        head = nums[0]; N = len(nums)
        lo, hi = 0, N - 1
        while(lo <= hi):
            mid = lo + (hi - lo) // 2
            if nums[mid] < head:
                hi = mid - 1
            else:
                lo = mid + 1
            
        return nums[lo % N]