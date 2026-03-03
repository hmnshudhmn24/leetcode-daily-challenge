class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        
        length = (1 << n) - 1
        mid = length // 2 + 1
        
        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            mirrored_bit = self.findKthBit(n - 1, length - k + 1)
            return "0" if mirrored_bit == "1" else "1"
