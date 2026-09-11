class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        from collections import Counter
        res = 0
        counts = Counter(digits)
        
        for i in range(100, 1000, 2):
            s = str(i)
            cur_counts = Counter(map(int, s))
            
            possible = True
            for d, count in cur_counts.items():
                if counts[d] < count:
                    possible = False
                    break
            
            if possible:
                res += 1
                
        return res
