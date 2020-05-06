# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        merged_list = ListNode(0)
        pointer = merged_list

        while True:
            if l1 is None and l2 is None:
                break
            elif l1 is None and l2 is not None:
                pointer.next = l2
                break
            elif l1 is not None and l2 is None:
                pointer.next = l1
                break
            else:
                if l1.val <= l2.val:
                    smaller_number = l1.val
                    l1 = l1.next
                else:
                    smaller_number = l2.val
                    l2 = l2.next

            append_node = ListNode(smaller_number)
            pointer.next = append_node
            pointer = pointer.next

        return merged_list.next


