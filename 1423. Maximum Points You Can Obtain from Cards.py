from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window_size = n - k
        min_sum = current_sum = sum(cardPoints[:window_size])
        
        for i in range(window_size, n):
            current_sum += cardPoints[i] - cardPoints[i - window_size]
            min_sum = min(min_sum, current_sum)
            
        return sum(cardPoints) - min_sum
