class Solution:
    def canAliceWin(self, n: int) -> bool:
        curr = 10
        alice_turn = True
        while n >= curr:
            n -= curr
            curr -= 1
            alice_turn = not alice_turn
        return not alice_turn
