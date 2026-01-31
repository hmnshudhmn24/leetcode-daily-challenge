class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Optimization: Early check for wrap-around case
        # If target is >= the largest character, the answer is the first character.
        if target >= letters[-1]:
            return letters[0]

        left, right = 0, len(letters) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # We are looking for something strictly greater than target
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
                
        # 'left' will point to the smallest element greater than target
        return letters[left]
