class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s2 = s + s
        ans = float('inf')
        diff1, diff2 = 0, 0
        
        for i, char in enumerate(s2):
            alt1 = '0' if i % 2 == 0 else '1'
            alt2 = '1' if i % 2 == 0 else '0'
            
            if char != alt1: 
                diff1 += 1
            if char != alt2: 
                diff2 += 1
            
            if i >= n:
                old_char = s2[i - n]
                old_alt1 = '0' if (i - n) % 2 == 0 else '1'
                old_alt2 = '1' if (i - n) % 2 == 0 else '0'
                
                if old_char != old_alt1: 
                    diff1 -= 1
                if old_char != old_alt2: 
                    diff2 -= 1
                
            if i >= n - 1:
                ans = min(ans, diff1, diff2)
                
        return ans
