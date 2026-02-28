from typing import List

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = ""
        
        for word in words:
            prefix += word
            if prefix == s:
                return True
            # If the built string overshoots the target string, we can stop early
            if len(prefix) > len(s):
                return False
                
        return False
