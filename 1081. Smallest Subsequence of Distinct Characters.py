class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occ = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()

        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last_occ[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)

        return "".join(stack)
