class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        return max(event1[0], event2[0]) <= min(event1[1], event2[1])
