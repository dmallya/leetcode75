from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxCandies = max(candies) - extraCandies
        for candy in candies:
            result.append(candy >= maxCandies)
        return result
