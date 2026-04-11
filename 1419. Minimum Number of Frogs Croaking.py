class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c = r = o = a = k = frogs = max_frogs = 0
        
        for char in croakOfFrogs:
            if char == 'c':
                c += 1
                frogs += 1
                max_frogs = max(max_frogs, frogs)
            elif char == 'r': r += 1
            elif char == 'o': o += 1
            elif char == 'a': a += 1
            elif char == 'k':
                k += 1
                frogs -= 1
            else:
                return -1
                
            if not (c >= r >= o >= a >= k):
                return -1
                
        if frogs == 0 and c == r == o == a == k:
            return max_frogs
            
        return -1
