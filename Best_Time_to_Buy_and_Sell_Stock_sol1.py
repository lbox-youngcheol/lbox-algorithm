class Solution:
    # slow
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            buy = prices[i]

            for j in range(i + 1, len(prices)):
                sell = prices[j]
                max_profit = max(max_profit, sell - buy)

        return max_profit


if __name__ == '__main__':
    assert Solution().maxProfit([7,1,5,3,6,4]) == 5
    assert Solution().maxProfit([7,6,4,3,1]) == 0
