class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = ""
        for i in range(len(number)):
            if number[i] == digit:
                res = max(res, number[:i] + number[i+1:])
        return res
