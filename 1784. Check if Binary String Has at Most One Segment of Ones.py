class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # If "01" is in the string, there is more than one segment of 1s.
        return "01" not in s
