from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = [0] * (len(A) + 1)
        C = []
        common = 0

        for a, b in zip(A, B):
            freq[a] += 1
            if freq[a] == 2:
                common += 1

            freq[b] += 1
            if freq[b] == 2:
                common += 1

            C.append(common)

        return C
