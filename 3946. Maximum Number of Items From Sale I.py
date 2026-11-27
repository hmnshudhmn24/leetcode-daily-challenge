class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        dp = [0] * (budget + 1)
        min_price = float('inf')

        for factor, price in items:
            min_price = min(min_price, price)
            count = sum(f % factor == 0 for f, _ in items)

            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + count)

        return max(dp[i] + (budget - i) // min_price for i in range(budget + 1))
