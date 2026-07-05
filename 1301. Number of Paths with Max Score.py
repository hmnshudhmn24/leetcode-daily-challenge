from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7

        dp = [[[-1, 0] for _ in range(n + 1)] for _ in range(n + 1)]
        dp[n - 1][n - 1] = [0, 1]

        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if board[r][c] == "S" or board[r][c] == "X":
                    continue

                curr_val = 0 if board[r][c] == "E" else int(board[r][c])
                max_prev_score = -1
                total_paths = 0

                for dr, dc in [(1, 0), (0, 1), (1, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and dp[nr][nc][0] != -1:
                        if dp[nr][nc][0] > max_prev_score:
                            max_prev_score = dp[nr][nc][0]
                            total_paths = dp[nr][nc][1]
                        elif dp[nr][nc][0] == max_prev_score:
                            total_paths = (total_paths + dp[nr][nc][1]) % MOD

                if max_prev_score != -1:
                    dp[r][c] = [max_prev_score + curr_val, total_paths]

        res = dp[0][0]
        return res if res[0] != -1 else [0, 0]
