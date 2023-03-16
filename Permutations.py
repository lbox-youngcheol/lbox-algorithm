from itertools import permutations
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [
            list(combination)
            for combination
            in permutations(nums, len(nums))
        ]
