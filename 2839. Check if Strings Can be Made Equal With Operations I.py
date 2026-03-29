class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return sorted(s1[0::2]) == sorted(s2[0::2]) and sorted(s1[1::2]) == sorted(s2[1::2])


# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.canBeEqual("abcd", "cdab"))  # True
