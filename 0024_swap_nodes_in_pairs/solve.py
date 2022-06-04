# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        dummy_node = ListNode(next=head)
        ptr = dummy_node

        while (n1 := ptr.next) and (n2 := n1.next):
            n3 = n2.next
            ptr.next = n2
            n2.next = n1
            n1.next = n3
            ptr = n1
        return dummy_node.next
