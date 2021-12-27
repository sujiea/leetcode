class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = 0
        slow = 0
        for i in nums:
            if i != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
