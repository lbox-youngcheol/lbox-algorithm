# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]


if __name__ == '__main__':
    assert Solution().findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2) == 5
    assert Solution().findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) == 4
