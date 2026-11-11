class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        a = min(cost1, costBoth)
        b = min(cost2, costBoth)
        minN = min(need1, need2)
        cost0 = need1 * a + need2 * b
        costMin = minN * costBoth + (need1 - minN) * a + (need2 - minN) * b
        return min(cost0, costMin)
