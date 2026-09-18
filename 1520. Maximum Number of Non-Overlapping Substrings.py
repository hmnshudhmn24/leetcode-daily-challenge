class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # 1. Find the first and last occurrence of each character
        first = {c: i for i, c in reversed(list(enumerate(s)))}
        last = {c: i for i, c in enumerate(s)}
        
        intervals = []
        
        # 2. Build valid intervals
        for char in set(s):
            start, end = first[char], last[char]
            
            # Try to extend this range to satisfy the condition
            i = start
            valid = True
            while i <= end:
                c = s[i]
                # If we find a char that started before our current range,
                # this specific range cannot be a valid independent substring.
                if first[c] < start:
                    valid = False
                    break
                
                # Extend the end to include all occurrences of the current char
                end = max(end, last[c])
                i += 1
            
            if valid:
                intervals.append([start, end])
        
        # 3. Greedy Selection (Activity Selection Problem)
        # Sort by end index to maximize the number of non-overlapping intervals
        intervals.sort(key=lambda x: x[1])
        
        result = []
        prev_end = -1
        
        for start, end in intervals:
            # If the current interval starts after the previous one ended, take it.
            # Note: Because of the nested property of valid substrings, strict 
            # inequality (> prev_end) ensures we don't pick a parent after picking a child.
            if start > prev_end:
                result.append(s[start : end + 1])
                prev_end = end
                
        return result
