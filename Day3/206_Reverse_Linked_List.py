from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        values = []

        while node:
            values.append(node.val)
            if node.next:
                node = node.next
            else:
                break
        values.reverse()

        node = head

        while node:
            node.val = values.pop(0)
            if node.next:
                node = node.next
            else:
                break

        return head
