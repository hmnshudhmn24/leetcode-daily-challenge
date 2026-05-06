class Solution:
    def rotateTheBox(self, box: list[list[str]]) -> list[list[str]]:
        m, n = len(box), len(box[0])

        for i in range(m):
            empty_spot = n - 1
            for j in range(n - 1, -1, -1):
                if box[i][j] == '*':
                    empty_spot = j - 1
                elif box[i][j] == '#':
                    box[i][j], box[i][empty_spot] = box[i][empty_spot], box[i][j]
                    empty_spot -= 1

        ans = [['.'] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                ans[j][m - 1 - i] = box[i][j]

        return ans
