class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        
        # Loop until both strings are exhausted and no carry remains
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            # If total is 0 or 2, append '0'. If 1 or 3, append '1'.
            res.append(str(total % 2))
            
            # If total is 2 or 3, new carry is 1. Otherwise 0.
            carry = total // 2
        
        # The result is constructed backwards, so reverse it
        return ''.join(res[::-1])
