class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack = []
        res = prices[:]
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                res[stack.pop()] -= prices[i]
            stack.append(i)
        return res
