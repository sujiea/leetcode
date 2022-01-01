from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 0
        count = len(nums)
        mid = 0
        min = len(nums)
        match = False
        while end < count or (end == count and mid >= target):
            if mid < target:
                end += 1
                mid += nums[end - 1]
            elif mid >= target:
                match = True
                if end - start < min:
                    min = end - start
                start += 1
                mid -= nums[start - 1]
        if match:
            return min
        else:
            return 0

nums = [1,1,1,1,1,1,1,1]
s = Solution()
print(s.minSubArrayLen(11,nums))
