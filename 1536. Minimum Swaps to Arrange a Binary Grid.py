class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        n = len(grid)
        trailing_zeros = []
        
        # Step 1: Count trailing zeros for each row
        for row in grid:
            zeros = 0
            for val in reversed(row):
                if val == 0:
                    zeros += 1
                else:
                    break
            trailing_zeros.append(zeros)
            
        swaps = 0
        
        # Step 2: Greedily place the correct row at each index
        for i in range(n):
            target = n - 1 - i
            found_idx = -1
            
            # Find the closest row that satisfies the target zeros
            for j in range(i, n):
                if trailing_zeros[j] >= target:
                    found_idx = j
                    break
                    
            # If no row has enough trailing zeros, the grid can't be valid
            if found_idx == -1:
                return -1
                
            # Step 3: Simulate the swaps 
            # We pop the found row and insert it at the current target index i
            # The number of swaps needed is exactly the distance it moved
            val = trailing_zeros.pop(found_idx)
            trailing_zeros.insert(i, val)
            
            swaps += (found_idx - i)
            
        return swaps
