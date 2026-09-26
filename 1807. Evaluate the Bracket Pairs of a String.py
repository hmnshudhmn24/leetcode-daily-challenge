from typing import List

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = dict(knowledge)
        parts = s.split('(')
        res = [parts[0]]
        
        for part in parts[1:]:
            key, rest = part.split(')')
            res.append(d.get(key, '?'))
            res.append(rest)
            
        return "".join(res)
