class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        res = [''] * len(s)
        for i, char in enumerate(s):
            res[indices[i]] = char
        return "".join(res)
