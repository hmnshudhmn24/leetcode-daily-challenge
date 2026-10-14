class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        q, r = divmod(sum, 9)
        res = "9" * q + (str(r) if r else "")
        return res + "0" * (num - len(res))
