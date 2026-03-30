class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even_freq = [0] * 26
        odd_freq = [0] * 26

        for i in range(len(s1)):
            v1 = ord(s1[i]) - 97
            v2 = ord(s2[i]) - 97

            if i % 2 == 0:
                even_freq[v1] += 1
                even_freq[v2] -= 1
            else:
                odd_freq[v1] += 1
                odd_freq[v2] -= 1

        return not any(even_freq) and not any(odd_freq)
