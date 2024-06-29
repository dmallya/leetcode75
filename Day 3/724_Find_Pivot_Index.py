from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums.insert(0, 0)
        rightSum = sum(nums)
        currentSum = 0
        for i in range(1, len(nums)):
            rightSum -= nums[i]
            currentSum += nums[i - 1]

            if rightSum == currentSum:
                return i - 1
        return -1
