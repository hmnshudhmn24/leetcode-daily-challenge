class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            # 1. Shift result to the left to make room for the new bit
            res = res << 1
            
            # 2. Get the last bit of n (n & 1) and add it to res
            #    (using bitwise OR | or addition + works the same here)
            bit = n & 1
            res = res | bit
            
            # 3. Shift n to the right to process the next bit
            n = n >> 1
            
        return res
