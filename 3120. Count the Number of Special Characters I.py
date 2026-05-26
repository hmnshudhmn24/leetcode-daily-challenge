class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        return sum(chr(i) in s and chr(i - 32) in s for i in range(97, 123))
