import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        max_heap = []
        
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0:
                heapq.heappush(max_heap, (count, char))
                
        while max_heap:
            count, char = heapq.heappop(max_heap)
            
            if len(res) >= 2 and res[-1] == res[-2] == char:
                if not max_heap:
                    break
                count2, char2 = heapq.heappop(max_heap)
                res.append(char2)
                if count2 + 1 < 0:
                    heapq.heappush(max_heap, (count2 + 1, char2))
                heapq.heappush(max_heap, (count, char))
            else:
                res.append(char)
                if count + 1 < 0:
                    heapq.heappush(max_heap, (count + 1, char))
                    
        return "".join(res)
