# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        ptr, current = head, head
        for _ in range(n):
            if current is None:
                return None
            current = current.next

        if current is None: # edge case
            return head.next
        else:
            current = current.next

        while current is not None:
            current = current.next
            ptr = ptr.next
        ptr.next = ptr.next.next

        return head
