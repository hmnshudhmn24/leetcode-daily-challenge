from collections import defaultdict

class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        total_len = n + m - 1
        word = ['?'] * total_len

        for i in range(n):
            if str1[i] == 'T':
                for k in range(m):
                    if word[i + k] != '?' and word[i + k] != str2[k]:
                        return ""
                    word[i + k] = str2[k]

        f_ends_at = defaultdict(list)

        for i in range(n):
            if str1[i] == 'F':
                last_q = -1
                possible_match = True

                for k in range(m):
                    if word[i + k] == '?':
                        last_q = i + k
                    elif word[i + k] != str2[k]:
                        possible_match = False
                        break

                if possible_match:
                    if last_q == -1:
                        return "" 
                    f_ends_at[last_q].append(i)

        for i in range(total_len):
            if word[i] == '?':
                for c in "abcdefghijklmnopqrstuvwxyz":
                    word[i] = c
                    is_valid = True

                    for start_idx in f_ends_at[i]:
                        window_matches = True
                        for k in range(m):
                            if word[start_idx + k] != str2[k]:
                                window_matches = False
                                break

                        if window_matches:
                            is_valid = False
                            break

                    if is_valid:
                        break 
                else:
                    return ""

        return "".join(word)
