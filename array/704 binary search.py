import math
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums)
        left = 0
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1

s = Solution()
num = [2,5]
print(s.search(num, 2))
