from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        pref = [0] * (len(words) + 1)
        for i, w in enumerate(words):
            pref[i+1] = pref[i] + (1 if w[0] in vowels and w[-1] in vowels else 0)
        return [pref[r+1] - pref[l] for l, r in queries]
