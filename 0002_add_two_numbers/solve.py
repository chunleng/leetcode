from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: Optional['ListNode']=None):
        self.val = val
        self.next = next

    pass

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current_l1, current_l2 = l1, l2
        ret = current_ret = ListNode()

        while current_l1 or current_l2:
            if current_ret.next is None:
                current_ret.next = ListNode()
            current_ret = current_ret.next

            if current_l1 is None:
                current_l1 = ListNode()
            if current_l2 is None:
                current_l2 = ListNode()

            place_total = current_l1.val + current_l2.val + current_ret.val
            if place_total > 9:
                current_ret.val = place_total - 10
                current_ret.next = ListNode(val=1)
            else:
                current_ret.val = place_total

            current_l1 = current_l1.next
            current_l2 = current_l2.next

        if ret.next is None:
            return ret
        return ret.next
