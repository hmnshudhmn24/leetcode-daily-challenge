class Solution:
    def minOperations(self, s: str) -> int:
        diff_0 = 0
        
        for i in range(len(s)):
            # If the index is even, the character should be '0'
            # If the index is odd, the character should be '1'
            if int(s[i]) != i % 2:
                diff_0 += 1
                
        return min(diff_0, len(s) - diff_0)
