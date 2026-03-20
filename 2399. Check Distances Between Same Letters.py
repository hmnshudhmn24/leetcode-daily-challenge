class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        first_pos = {}
        for i, char in enumerate(s):
            if char in first_pos:
                if i - first_pos[char] - 1 != distance[ord(char) - ord('a')]:
                    return False
            else:
                first_pos[char] = i
                
        return True
