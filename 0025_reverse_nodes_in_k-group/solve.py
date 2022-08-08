# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 1:
            return head

        dummy_node = ListNode(next=head)
        ptr = dummy_node

        while ptr:
            before_head = ptr
            head = ptr.next
            for _ in range(k):
                ptr = ptr.next
                if not ptr:
                    return dummy_node.next
            self.reverseLinkedListInternal(before_head, ptr)
            ptr = head # after reversing, the head is the new end

    def reverseLinkedListInternal(self, before_head: ListNode, end: ListNode):
        sorted_head = before_head.next
        if not sorted_head:
            return # this shouldn't happen if the function is used correctly
        unsorted_head = sorted_head.next
        before_head.next = end      # the end node will be the new first node
        sorted_head.next = end.next # the first node will be the new end node

        while sorted_head != end:
            # Push the unsorted head to the sorted
            temp = unsorted_head.next
            unsorted_head.next = sorted_head
            sorted_head = unsorted_head
            unsorted_head = temp

