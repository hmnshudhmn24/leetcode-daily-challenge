class Solution:
    def countTestedDevices(self, batteryPercentages: list[int]) -> int:
        tested = 0
        for battery in batteryPercentages:
            if battery - tested > 0:
                tested += 1
        return tested
