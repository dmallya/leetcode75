# Optimal Solution by Darshan0902

from typing import List


class Solution:
    def findMaxAverage(nums: List[int], k: int) -> float:
        max_sum = current_sum = sum(nums[:k])

        for i in range(len(nums) - k):
            current_sum = current_sum - nums[i] + nums[i + k]
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum / k
