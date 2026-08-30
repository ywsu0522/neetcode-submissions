class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lo, hi = 0, len(heights) - 1
        vol = (hi - lo) * min(heights[lo], heights[hi])

        while (lo < hi):
            if heights[lo] > heights[hi]:
                hi -= 1
            else:
                lo += 1
            
            vol = max(vol, (hi - lo) * min(heights[lo], heights[hi]))

        return vol