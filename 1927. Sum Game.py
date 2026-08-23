class Solution:
    def sumGame(self, num: str) -> bool:
        mid = len(num) // 2

        s_l = sum(int(c) for c in num[:mid] if c != '?')
        s_r = sum(int(c) for c in num[mid:] if c != '?')

        q_l = num[:mid].count('?')
        q_r = num[mid:].count('?')

        if (q_l + q_r) % 2 != 0:
            return True

        return 2 * (s_l - s_r) + (q_l - q_r) * 9 != 0
