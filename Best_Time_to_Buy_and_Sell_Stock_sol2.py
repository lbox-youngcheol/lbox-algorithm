class Solution:
    # fast
    """
    훑으면서 현재까지의 최저가와 현재 가격을 빼면서 최대 이익인지 확인한다
    """
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')  # means positive infinity
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(price - min_price, max_profit)

        return max_profit


if __name__ == '__main__':
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
