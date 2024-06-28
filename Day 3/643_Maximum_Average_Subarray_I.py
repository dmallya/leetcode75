from typing import List


class Solution:
    def findMaxAverage(nums: List[int], k: int) -> float:
        left = 0
        right = k
        max_average = float()

        if len(nums) == 1:
            return nums[0]

        while right <= len(nums):
            max_average = max(sum(nums[left:right]) / k, max_average)
            left += 1
            right += 1
        return max_average

    print(findMaxAverage([0, 1, 1, 3, 3], 4))
