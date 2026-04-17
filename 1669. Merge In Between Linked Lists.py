class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        pre_a = list1
        for _ in range(a - 1):
            pre_a = pre_a.next

        after_b = pre_a
        for _ in range(b - a + 2):
            after_b = after_b.next

        pre_a.next = list2

        last_node_list2 = list2
        while last_node_list2.next:
            last_node_list2 = last_node_list2.next

        last_node_list2.next = after_b
        return list1
