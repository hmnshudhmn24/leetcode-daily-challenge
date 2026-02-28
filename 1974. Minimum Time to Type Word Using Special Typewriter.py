class Solution:
    def minTimeToType(self, word: str) -> int:
        total_time = 0
        current_char = 'a'
        
        for char in word:
            # Absolute difference in ASCII values
            diff = abs(ord(char) - ord(current_char))
            
            # Shortest path: either direct or wrapping around the circle
            min_dist = min(diff, 26 - diff)
            
            # Add movement time + 1 second to type
            total_time += min_dist + 1
            current_char = char
            
        return total_time
