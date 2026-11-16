class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            next_s = []
            for i in range(0, len(s), k):
                chunk = s[i:i+k]
                next_s.append(str(sum(int(d) for d in chunk)))
            s = "".join(next_s)
        return s
