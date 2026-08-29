class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxlen = 0
        for n in nums:
            if n - 1 in nums_set:
                continue
            
            n_len = 1
            while (n + n_len in nums_set):
                n_len += 1

            maxlen = max(maxlen, n_len)

        return maxlen

