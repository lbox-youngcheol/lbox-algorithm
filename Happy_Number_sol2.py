# https://leetcode.com/problems/happy-number/

class Solution:
    """
    Set을 사용하지 않는 솔루션
    - 하나의 포인터는 한 단계 씩 계산을 진행한다.
    - 또다른 포인터는 두 단계 씩 계산을 진행한다.
    만약 한 포인터가 1이 되면 happy number 임이 확인이 되고,
    두 포인터가 1이 아닌데 서로 만나게되면 loop를 돈다는 의미이므로 happy number가 아님이 확인된다.
    """
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n

        while True:
            slow = self.next_step_number(slow)
            fast = self.next_step_number(self.next_step_number(fast))  # run as twice as slow

            if (slow == 1) or (fast == 1):
                return True

            if slow == fast:
                return False

    def next_step_number(self, number: int) -> int:
        return sum([int(digit)**2 for digit in str(number)])


if __name__ == '__main__':
    assert Solution().isHappy(n=7)
    assert not Solution().isHappy(n=2)
    assert Solution().isHappy(n=19)
