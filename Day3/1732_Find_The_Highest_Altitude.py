from typing import List


class Solution:
    def largestAltitude(gain: List[int]) -> int:
        prefixSum = []
        curSum = 0
        for num in gain:
            curSum += num
            prefixSum.append(curSum)

        return max(prefixSum)

    print(largestAltitude([-4, -3, -2, -1, 4, 3, 2]))
