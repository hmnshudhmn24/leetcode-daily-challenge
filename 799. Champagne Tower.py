class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Create a 2D table to store the amount of champagne in each glass.
        # We need size up to query_row + 2 to handle the overflow from the last row safely.
        # Using 102 as a safe upper bound since query_row <= 99.
        tower = [[0.0] * 102 for _ in range(102)]
        
        # Pour everything into the top glass
        tower[0][0] = float(poured)
        
        # Iterate through each row to process the overflow
        for r in range(query_row + 1):
            for c in range(r + 1):
                # If this glass has overflowed
                if tower[r][c] > 1:
                    excess = (tower[r][c] - 1.0) / 2.0
                    tower[r][c] = 1.0  # The current glass stays full
                    tower[r+1][c] += excess     # Flow to bottom-left
                    tower[r+1][c+1] += excess   # Flow to bottom-right
                    
        # Return the amount in the target glass, capped at 1.0
        return min(1.0, tower[query_row][query_glass])
