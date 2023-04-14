# https://leetcode.com/problems/single-number/
from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        least_common_num, _1 = Counter(nums).most_common()[-1]
        assert _1 == 1
        return least_common_num


if __name__ == '__main__':
    assert Solution().singleNumber([2, 2, 1]) == 1
    assert Solution().singleNumber([4, 1, 2, 1, 2]) == 4
    assert Solution().singleNumber([1]) == 1
