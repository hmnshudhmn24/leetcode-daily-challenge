class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        substrings = []
        
        # Iterate through the string to identify top-level special substrings
        for j, char in enumerate(s):
            count += 1 if char == '1' else -1
            
            # When count returns to 0, we found a complete special substring s[i:j+1]
            if count == 0:
                # The structure is "1" + inner + "0"
                # We recursively maximize the inner part: s[i+1:j]
                inner = self.makeLargestSpecial(s[i+1:j])
                
                # Reconstruct the string with the optimized inner part
                substrings.append("1" + inner + "0")
                
                # Move start pointer for the next substring
                i = j + 1
        
        # Sort substrings in descending order to make it lexicographically largest
        substrings.sort(reverse=True)
        
        return "".join(substrings)
