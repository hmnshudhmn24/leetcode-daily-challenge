class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefix_days = [0] * 13
        
        for i in range(1, 13):
            prefix_days[i] = prefix_days[i - 1] + days_in_month[i - 1]
        
        def to_days(date_str):
            m, d = int(date_str[:2]), int(date_str[3:])
            return prefix_days[m] + d
        
        a_start, a_end = to_days(arriveAlice), to_days(leaveAlice)
        b_start, b_end = to_days(arriveBob), to_days(leaveBob)
        
        start = max(a_start, b_start)
        end = min(a_end, b_end)
        
        return max(0, end - start + 1)
