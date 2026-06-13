from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        return "".join(chr(122 - (sum(weights[ord(c) - 97] for c in w) % 26)) for w in words)
