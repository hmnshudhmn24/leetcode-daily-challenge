class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: list[int], experience: list[int]) -> int:
        hours = 0
        req_energy = sum(energy) + 1
        
        if initialEnergy < req_energy:
            hours += req_energy - initialEnergy
        
        curr_exp = initialExperience
        for exp in experience:
            if curr_exp <= exp:
                diff = exp - curr_exp + 1
                hours += diff
                curr_exp += diff
            curr_exp += exp
            
        return hours
