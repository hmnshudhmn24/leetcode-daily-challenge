class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (1 << (n - 1))
        if k > total:
            return ""
        
        k -= 1
        res = []
        choices = ['a', 'b', 'c']
        block_size = 1 << (n - 1)
        
        res.append(choices[k // block_size])
        k %= block_size
        
        for i in range(n - 1):
            block_size >>= 1
            valid = [c for c in choices if c != res[-1]]
            res.append(valid[k // block_size])
            k %= block_size
            
        return "".join(res)
