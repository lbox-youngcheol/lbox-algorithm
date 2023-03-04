# https://leetcode.com/problems/happy-number/

class Solution:
    """
    1이 될 때까지 각 자리수의 제곱을 서로 더한다.
    단 각 계산 단계에서 이전에 계산된 수를 다시 마주친다면 계속 루프를 돌 것이기 때문에 happy number가 될 수 없다.
    """
    def isHappy(self, n: int) -> bool:
        visited: set[int] = set()

        while n != 1:
            n = sum(i**2 for i in self.split_digits(n))

            if n in visited:
                return False

            visited.add(n)

        return True

    def split_digits(self, number: int) -> list[int]:
        return [int(digit) for digit in str(number)]


if __name__ == '__main__':
    assert Solution().isHappy(n=7)
    assert not Solution().isHappy(n=2)
    assert Solution().isHappy(n=19)
