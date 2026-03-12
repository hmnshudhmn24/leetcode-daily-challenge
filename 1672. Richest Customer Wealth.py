from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            current_wealth = sum(customer)
            if current_wealth > max_wealth:
                max_wealth = current_wealth
        return max_wealth
