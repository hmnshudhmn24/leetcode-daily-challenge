from typing import List

class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        collected = set()
        sequence_len = 0
        
        for roll in rolls:
            collected.add(roll)
            if len(collected) == k:
                sequence_len += 1
                collected.clear()
                
        return sequence_len + 1
