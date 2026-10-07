class Solution:
    def removeInvalidParentheses(self, s: str):
        res = set()

        lremove = rremove = 0
        for c in s:
            if c == '(':
                lremove += 1
            elif c == ')':
                if lremove > 0:
                    lremove -= 1
                else:
                    rremove += 1

        def is_valid(string):
            count = 0
            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        def dfs(index, path, lcount, rcount, lremove, rremove):
            if index == len(s):
                if lremove == 0 and rremove == 0 and is_valid(path):
                    res.add(path)
                return

            char = s[index]

            if char == '(':
                if lremove > 0:
                    dfs(index + 1, path, lcount, rcount, lremove - 1, rremove)
                dfs(index + 1, path + char, lcount + 1, rcount, lremove, rremove)

            elif char == ')':
                if rremove > 0:
                    dfs(index + 1, path, lcount, rcount, lremove, rremove - 1)
                if lcount > rcount:
                    dfs(index + 1, path + char, lcount, rcount + 1, lremove, rremove)

            else:
                dfs(index + 1, path + char, lcount, rcount, lremove, rremove)

        dfs(0, "", 0, 0, lremove, rremove)
        return list(res)
