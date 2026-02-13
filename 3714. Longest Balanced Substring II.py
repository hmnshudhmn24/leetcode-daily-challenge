class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        # Case 1: One distinct character (longest consecutive streak)
        count = 0
        for i in range(n):
            if i > 0 and s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            ans = max(ans, count)
            
        # Case 2: Two distinct characters (a-b, b-c, a-c)
        def solve_two(char1, char2):
            res = 0
            # Map stores first occurrence of (count1 - count2)
            # We clear it whenever the 3rd character appears to ensure "only distinct" characters
            pos = {0: -1}
            diff = 0
            for i, char in enumerate(s):
                if char == char1:
                    diff += 1
                elif char == char2:
                    diff -= 1
                else:
                    # Reset when third character breaks the "two-character" constraint
                    diff = 0
                    pos = {0: i}
                    continue
                
                if diff in pos:
                    res = max(res, i - pos[diff])
                else:
                    pos[diff] = i
            return res

        ans = max(ans, solve_two('a', 'b'), solve_two('b', 'c'), solve_two('a', 'c'))

        # Case 3: Three distinct characters (a, b, and c)
        # We need count(a) == count(b) AND count(b) == count(c)
        # This is equivalent to: (count(a)-count(b) == 0) AND (count(b)-count(c) == 0)
        counts = {'a': 0, 'b': 0, 'c': 0}
        pos_three = {(0, 0): -1}
        for i, char in enumerate(s):
            counts[char] += 1
            # State is the pair of differences
            state = (counts['a'] - counts['b'], counts['b'] - counts['c'])
            
            if state in pos_three:
                ans = max(ans, i - pos_three[state])
            else:
                pos_three[state] = i
                
        return ans
