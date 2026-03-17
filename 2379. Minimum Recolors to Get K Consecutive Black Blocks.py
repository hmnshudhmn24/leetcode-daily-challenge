class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_recolors = blocks[:k].count('W')
        current_recolors = min_recolors
        
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                current_recolors -= 1
            if blocks[i] == 'W':
                current_recolors += 1
            min_recolors = min(min_recolors, current_recolors)
            
        return min_recolors
