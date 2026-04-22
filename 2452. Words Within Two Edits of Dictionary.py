from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for q in queries:
            for d in dictionary:
                if sum(c1 != c2 for c1, c2 in zip(q, d)) <= 2:
                    ans.append(q)
                    break
        return ans
