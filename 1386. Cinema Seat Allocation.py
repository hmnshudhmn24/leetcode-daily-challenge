from typing import List
import collections

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = collections.defaultdict(set)
        for r, c in reservedSeats:
            if c in (2, 3, 4, 5, 6, 7, 8, 9):
                seats[r].add(c)
                
        res = (n - len(seats)) * 2
        
        for r in seats:
            left = not seats[r] & {2, 3, 4, 5}
            right = not seats[r] & {6, 7, 8, 9}
            mid = not seats[r] & {4, 5, 6, 7}
            
            if left and right:
                res += 2
            elif left or right or mid:
                res += 1
                
        return res
