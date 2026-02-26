class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> list[int]:
        if tomatoSlices % 2 != 0:
            return []
        jumbo = tomatoSlices // 2 - cheeseSlices
        small = cheeseSlices - jumbo
        if jumbo >= 0 and small >= 0:
            return [jumbo, small]
        return []
