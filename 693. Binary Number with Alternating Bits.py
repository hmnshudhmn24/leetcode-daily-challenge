class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Get the very last bit
        last_bit = n % 2
        n //= 2  # Shift right (remove the last bit)
        
        while n > 0:
            current_bit = n % 2
            
            # If two adjacent bits are the same, it's not alternating
            if current_bit == last_bit:
                return False
            
            # Update last_bit and shift n
            last_bit = current_bit
            n //= 2
            
        return True
