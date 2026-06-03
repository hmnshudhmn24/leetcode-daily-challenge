class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        min_land = min(s + d for s, d in zip(landStartTime, landDuration))
        min_water = min(s + d for s, d in zip(waterStartTime, waterDuration))

        l_then_w = min(max(min_land, ws) + wd for ws, wd in zip(waterStartTime, waterDuration))
        w_then_l = min(max(min_water, ls) + ld for ls, ld in zip(landStartTime, landDuration))

        return min(l_then_w, w_then_l)
