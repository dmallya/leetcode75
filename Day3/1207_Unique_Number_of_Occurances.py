from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrCount = Counter(arr)
        return len(set(arrCount.values())) == len(arrCount.values())
