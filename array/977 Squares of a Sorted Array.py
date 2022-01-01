import math


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        square = [0] * len(nums)
        i = len(nums) - 1
        right_square = nums[right] ** 2
        left_square = nums[left] ** 2
        while left < right:
            if left_square <= right_square:
                square[i] = right_square
                right -= 1
                right_square = nums[right] ** 2
            else:
                square[i] = left_square
                left += 1
                left_square = int(math.pow(nums[left], 2))
            i -= 1
        square[i] = int(math.pow(nums[left], 2))
        return square
