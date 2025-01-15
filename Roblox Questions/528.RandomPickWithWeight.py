# 528. Random Pick with Weight
# https://leetcode.com/problems/random-pick-with-weight/description/

import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        total = 0

        for weight in w:
            total += weight
            self.prefix_sums.append(total)
        
        self.total = total

    def pickIndex(self) -> int:
        target = random.uniform(0, self.total)

        l = 0
        r = len(self.prefix_sums)

        while l < r:
            mid = (l+r)//2

            if self.prefix_sums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        return l