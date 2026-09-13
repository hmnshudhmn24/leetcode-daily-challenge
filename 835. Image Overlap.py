import collections
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        counts = collections.defaultdict(int)
        max_overlap = 0
        
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift = (r2 - r1, c2 - c1)
                counts[shift] += 1
                if counts[shift] > max_overlap:
                    max_overlap = counts[shift]
                    
        return max_overlap
