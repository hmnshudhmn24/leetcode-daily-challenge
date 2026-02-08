from typing import List
import bisect

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # Helper function: KMP Algorithm to find all occurrences of a pattern
        def get_occurrences(text: str, pattern: str) -> List[int]:
            if not pattern:
                return []
            
            n, m = len(text), len(pattern)
            pi = [0] * m
            
            # Build prefix table (LPS array)
            j = 0
            for i in range(1, m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = pi[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                pi[i] = j
            
            # Search pattern in text
            indices = []
            j = 0
            for i in range(n):
                while j > 0 and text[i] != pattern[j]:
                    j = pi[j - 1]
                if text[i] == pattern[j]:
                    j += 1
                if j == m:
                    indices.append(i - m + 1)
                    j = pi[j - 1]
            return indices

        indices_a = get_occurrences(s, a)
        indices_b = get_occurrences(s, b)
        
        ans = []
        for i in indices_a:
            idx = bisect.bisect_left(indices_b, i - k)
            if idx < len(indices_b) and abs(indices_b[idx] - i) <= k:
                ans.append(i)
                
        return ans
