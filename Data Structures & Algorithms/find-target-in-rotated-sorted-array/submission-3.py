class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # First find the head
        lo, hi = 0, len(nums) - 1
        while (lo <= hi):
            mid = (lo + hi) // 2
            if (mid == hi):
                break
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid

        head = hi
        N = len(nums)
        # Ordinary binary search
        lo, hi = 0, N   # head, head
        while (lo < hi):
            mid = (lo + hi) // 2
            mid_true = (mid + head) % N
            if nums[mid_true] == target:
                return mid_true

            if nums[mid_true] < target:
                lo = mid + 1
            else:
                hi = mid

        return -1

