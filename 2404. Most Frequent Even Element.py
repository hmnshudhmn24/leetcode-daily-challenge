from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        counts = Counter(x for x in nums if x % 2 == 0)
        
        if not counts:
            return -1
            
        max_freq = max(counts.values())
        return min(k for k, v in counts.items() if v == max_freq)
