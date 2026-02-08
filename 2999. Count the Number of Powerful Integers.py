class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        
        # Pre-check: If any digit in 's' exceeds 'limit', no powerful integer can exist.
        for char in s:
            if int(char) > limit:
                return 0

        # Helper function to count powerful integers <= n (treated as a string)
        def count(n_val):
            s_n = str(n_val)
            n_len = len(s_n)
            s_len = len(s)
            
            # If the upper bound is shorter than the suffix, no powerful number fits.
            if n_len < s_len:
                return 0
            
            total_count = 0
            
            # --- Part 1: Count numbers with length strictly less than n_len ---
            for length in range(s_len, n_len):
                prefix_len = length - s_len
                
                if prefix_len == 0:
                    if s == "0" or s[0] != '0': 
                        total_count += 1
                else:
                    first_digit_choices = limit
                    other_digit_choices = limit + 1
                    
                    if first_digit_choices > 0:
                        total_count += first_digit_choices * (other_digit_choices ** (prefix_len - 1))

            # --- Part 2: Count numbers with length EQUAL to n_len ---
            target_prefix_len = n_len - s_len
            memo = {}

            def dfs(idx, is_tight):
                if idx == target_prefix_len:
                    if is_tight:
                        return 1 if s <= s_n[target_prefix_len:] else 0
                    else:
                        return 1
                
                state = (idx, is_tight)
                if state in memo:
                    return memo[state]
                
                digit_from_n = int(s_n[idx])
                upper_bound = digit_from_n if is_tight else 9
                
                res = 0
                for d in range(upper_bound + 1):
                    if d > limit:
                        break
                    if idx == 0 and target_prefix_len > 0 and d == 0:
                        continue
                    
                    new_tight = is_tight and (d == digit_from_n)
                    res += dfs(idx + 1, new_tight)
                
                memo[state] = res
                return res

            total_count += dfs(0, True)
            return total_count

        return count(finish) - count(start - 1)
