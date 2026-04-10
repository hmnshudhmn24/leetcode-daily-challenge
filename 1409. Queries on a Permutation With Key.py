from typing import List

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = list(range(1, m + 1))
        res = []
        
        for q in queries:
            idx = P.index(q)
            res.append(idx)
            P.insert(0, P.pop(idx))
            
        return res
