class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        def get_factors(n):
            if n == 0:
                return [0] * 8, False
            c = [0] * 8
            for p in (2, 3, 5, 7):
                while n % p == 0:
                    c[p] += 1
                    n //= p
            return c, n == 1

        req_counts, is_div = get_factors(t)
        if not is_div:
            return "-1"

        def min_digits(c2, c3, c5, c7):
            c9 = c3 // 2
            r3 = c3 % 2
            c8 = c2 // 3
            r2 = c2 % 3
            c4 = r2 // 2
            r2 %= 2
            c6 = 0
            if r2 == 1 and r3 == 1:
                r2 = r3 = 0
                c6 = 1
            elif r3 == 1 and c4 == 1:
                r2, c6, r3, c4 = 1, 1, 0, 0
            return c9 + c8 + c7 + c5 + c6 + c4 + r3 + r2

        def construct_optimal(c2, c3, c5, c7, total_len):
            c9 = c3 // 2
            r3 = c3 % 2
            c8 = c2 // 3
            r2 = c2 % 3
            c4 = r2 // 2
            r2 %= 2
            c6 = 0
            if r2 == 1 and r3 == 1:
                r2 = r3 = 0
                c6 = 1
            elif r3 == 1 and c4 == 1:
                r2, c6, r3, c4 = 1, 1, 0, 0
            res = ['9']*c9 + ['8']*c8 + ['7']*c7 + ['6']*c6 + ['5']*c5 + ['4']*c4 + ['3']*r3 + ['2']*r2
            res += ['1'] * (total_len - len(res))
            res.sort()
            return ''.join(res)

        req_len = min_digits(req_counts[2], req_counts[3], req_counts[5], req_counts[7])
        if req_len > len(num):
            return construct_optimal(req_counts[2], req_counts[3], req_counts[5], req_counts[7], req_len)

        zero_idx = num.find('0')
        first_zero = zero_idx if zero_idx != -1 else len(num)

        pref = [[0]*8]
        cur = [0]*8
        for ch in num:
            v = int(ch)
            if v > 0:
                c,_ = get_factors(v)
                for p in (2,3,5,7):
                    cur[p] += c[p]
            pref.append(cur.copy())

        if first_zero == len(num) and all(cur[p] >= req_counts[p] for p in (2,3,5,7)):
            return num

        for i in range(min(len(num)-1, first_zero), -1, -1):
            pref_c = pref[i]
            for d in range(int(num[i])+1, 10):
                c_d,_ = get_factors(d)
                r2=max(0, req_counts[2]-pref_c[2]-c_d[2])
                r3=max(0, req_counts[3]-pref_c[3]-c_d[3])
                r5=max(0, req_counts[5]-pref_c[5]-c_d[5])
                r7=max(0, req_counts[7]-pref_c[7]-c_d[7])
                avail=len(num)-1-i
                if min_digits(r2,r3,r5,r7) <= avail:
                    return num[:i] + str(d) + construct_optimal(r2,r3,r5,r7,avail)

        return construct_optimal(req_counts[2], req_counts[3], req_counts[5], req_counts[7], max(req_len, len(num)+1))
