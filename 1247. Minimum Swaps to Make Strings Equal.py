from typing import List

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        filtered = []
        
        for r in restaurants:
            if veganFriendly and not r[2]:
                continue
            if r[3] > maxPrice or r[4] > maxDistance:
                continue
            filtered.append(r)
        
        filtered.sort(key=lambda x: (-x[1], -x[0]))
        
        return [r[0] for r in filtered]
