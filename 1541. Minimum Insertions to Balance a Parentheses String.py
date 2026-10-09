class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        expected_right = 0
        
        for c in s:
            if c == '(':
                if expected_right % 2 != 0:
                    insertions += 1
                    expected_right -= 1
                expected_right += 2
            else:
                expected_right -= 1
                if expected_right < 0:
                    insertions += 1
                    expected_right = 1
                    
        return insertions + expected_right
