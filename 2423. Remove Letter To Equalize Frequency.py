from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            c = Counter(word[:i] + word[i+1:])
            if len(set(c.values())) == 1:
                return True
        return False
