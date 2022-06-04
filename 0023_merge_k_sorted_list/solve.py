# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        worklists = [l for l in lists if l is not None]
        if len(worklists) == 0:
            return None
        worklists.sort(key=lambda l:l.val)

        sorted_list = worklists.pop(0)
        ptr: ListNode = sorted_list

        def attempt_insert(item, lst):
            if item is not None:
                # Try to put it in the worklists
                inserted = False
                for i in range(len(lst)):
                    if item.val < lst[i].val:
                        lst.insert(i, item)
                        inserted = True
                        break
                if not inserted:
                    lst.append(item)

        attempt_insert(ptr.next, worklists)

        while len(worklists) > 0:
            ptr.next = worklists.pop(0)
            ptr = ptr.next
            attempt_insert(ptr.next, worklists)

        return sorted_list
