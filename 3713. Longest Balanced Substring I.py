class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        for i in range(n):
            cnt = {}
            distinct_count = 0
            max_freq = 0
            
            for j in range(i, n):
                char = s[j]
                
                # Update frequency
                cnt[char] = cnt.get(char, 0) + 1
                
                # Update distinct count and max frequency
                if cnt[char] == 1:
                    distinct_count += 1
                max_freq = max(max_freq, cnt[char])
                
                # Check condition: Distinct * MaxFreq == Length
                current_len = j - i + 1
                if distinct_count * max_freq == current_len:
                    ans = max(ans, current_len)
                    
        return ans
