class Solution:
    def processStr(self, s: str, k: int) -> str:
        tibrelkano = s
        operations = []
        curr_len = 0

        for ch in s:
            if 'a' <= ch <= 'z':
                if curr_len + 1 > 10**15:
                    break
                curr_len += 1
                operations.append((ch, curr_len))
            elif ch == '*':
                if curr_len > 0:
                    curr_len -= 1
                    operations.append(('*', curr_len))
            elif ch == '#':
                if curr_len * 2 > 10**15:
                    curr_len = 10**15 + 1
                else:
                    curr_len *= 2
                operations.append(('#', curr_len))
            elif ch == '%':
                operations.append(('%', curr_len))

        if k >= curr_len:
            return '.'

        def trace(k, ops):
            for i in range(len(ops) - 1, -1, -1):
                op, length = ops[i]
                prev_len = ops[i - 1][1] if i > 0 else 0

                if op == '*':
                    if k >= length:
                        continue
                elif 'a' <= op <= 'z':
                    if k == length - 1:
                        return op
                elif op == '#':
                    half = prev_len
                    if k >= half:
                        k -= half
                elif op == '%':
                    if length > 0:
                        k = length - 1 - k

        return trace(k, operations)
