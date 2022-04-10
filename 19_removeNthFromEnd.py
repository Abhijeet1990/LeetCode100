# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        # traverse a linked list
        curr = head
        curr2 = head
        node_count = 0
        while curr != None:
            curr = curr.next
            node_count += 1
        new_count = 0
        new_head = prev = None
        while curr2 != None:
            node = ListNode(curr2.val)
            if new_count != node_count - n:
                if prev is not None:
                    prev.next = node
                prev = node
            new_count += 1

            if new_head is None:
                new_head = prev
            curr2 = curr2.next
        return new_head
