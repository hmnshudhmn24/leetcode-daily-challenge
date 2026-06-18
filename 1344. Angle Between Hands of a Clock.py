class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h_angle = (hour % 12 * 30) + (minutes * 0.5)
        m_angle = minutes * 6
        diff = abs(h_angle - m_angle)
        return min(diff, 360 - diff)
