from functools import cache

class Solution:
    def totalWaviness(self, num1: str, num2: str) -> int:
        def solve(s: str) -> int:
            @cache
            def dp(i: int, p1: int, p2: int, tight: bool, lead: bool) -> tuple[int, int]:
                if i == len(s):
                    return 1, 0

                limit = int(s[i]) if tight else 9
                total_ways = 0
                total_waves = 0

                for d in range(limit + 1):
                    is_tight = tight and d == limit
                    is_lead = lead and d == 0
                    next_p1 = -1 if is_lead else d
                    next_p2 = -1 if lead else p1

                    ways, waves = dp(i + 1, next_p1, next_p2, is_tight, is_lead)
                    total_ways += ways
                    total_waves += waves

                    if not is_lead and p1 != -1 and p2 != -1:
                        if (p2 > p1 and d > p1) or (p2 < p1 and d < p1):
                            total_waves += ways

                return total_ways, total_waves

            return dp(0, -1, -1, True, True)[1]

        def check_val(s: str) -> int:
            waves = 0
            for i in range(1, len(s) - 1):
                p2, p1, d = int(s[i-1]), int(s[i]), int(s[i+1])
                if (p2 > p1 and d > p1) or (p2 < p1 and d < p1):
                    waves += 1
            return waves

        return solve(str(num2)) - solve(str(num1)) + check_val(str(num1))
