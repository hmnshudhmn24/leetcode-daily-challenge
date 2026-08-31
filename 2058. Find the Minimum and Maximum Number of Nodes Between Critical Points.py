class Solution:
    def nodesBetweenCriticalPoints(self, head) -> list[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first = -1
        last = -1
        min_d = float('inf')

        prev = head
        curr = head.next
        nxt = curr.next
        i = 1

        while nxt:
            if (curr.val > prev.val and curr.val > nxt.val) or (curr.val < prev.val and curr.val < nxt.val):
                if first == -1:
                    first = i
                else:
                    min_d = min(min_d, i - last)
                last = i

            prev = curr
            curr = nxt
            nxt = nxt.next
            i += 1

        if min_d == float('inf'):
            return [-1, -1]

        return [min_d, last - first]
