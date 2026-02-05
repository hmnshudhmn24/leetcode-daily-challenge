class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        s = [""] * n
        current_char = 'a'
        
        # Phase 1: Construct the string greedily
        for i in range(n):
            if s[i]: continue # Already assigned
            
            if current_char > 'z':
                return "" # Ran out of characters
                
            s[i] = current_char
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    s[j] = current_char
            
            current_char = chr(ord(current_char) + 1)
            
        # Check if any position was left unassigned (rare logic catch)
        if any(c == "" for c in s):
            return ""

        # Phase 2: Validate the constructed string against the LCP matrix
        # We iterate backwards to use the DP relationship: lcp[i][j] = 1 + lcp[i+1][j+1]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == s[j]:
                    expected_val = 1
                    if i + 1 < n and j + 1 < n:
                        expected_val += lcp[i+1][j+1]
                    
                    if lcp[i][j] != expected_val:
                        return ""
                else:
                    if lcp[i][j] != 0:
                        return ""
                        
        return "".join(s)
