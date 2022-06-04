# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            sorted_list = list1
            list1 = list1.next
        else:
            sorted_list = list2
            list2 = list2.next

        ptr = sorted_list
        while list1 and list2:
            if list1.val < list2.val:
                ptr.next = list1
                ptr = ptr.next
                list1 = list1.next
            else:
                ptr.next = list2
                ptr = ptr.next
                list2 = list2.next

        if list1 is None:
            ptr.next = list2
        else:
            ptr.next = list1


        return sorted_list
