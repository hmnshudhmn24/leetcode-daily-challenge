class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # A binary code of length k has 2^k possible combinations
        required_count = 1 << k 
        
        # Hash set to store unique substrings of length k
        seen = set()
        
        # Iterate through the string and extract all substrings of length k
        for i in range(len(s) - k + 1):
            seen.add(s[i:i+k])
            
            # Early optimization: if we found all combinations, stop checking
            if len(seen) == required_count:
                return True
                
        # If we finished the loop, check if we collected enough unique codes
        return len(seen) == required_count
