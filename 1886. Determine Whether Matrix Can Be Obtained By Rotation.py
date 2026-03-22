from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            # Rotate matrix 90 degrees clockwise
            mat = [list(x) for x in zip(*mat[::-1])]
            
        return False
