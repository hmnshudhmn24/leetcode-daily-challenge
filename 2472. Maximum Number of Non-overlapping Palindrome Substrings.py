class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        intervals = []
        
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) >= k:
                    intervals.append((l, r))
                    break 
                l -= 1
                r += 1
        
        for i in range(n):
            expand(i, i)
            expand(i, i + 1)
        
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        last_end = -1
        
        for start, end in intervals:
            if start > last_end:
                count += 1
                last_end = end
                
        return count
