# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        
        nodes = {0: None}

        count = 1
        while cur != None:
            nodes[count] = cur
            cur = cur.next
            count += 1
        
        
        idx = count - n
        
        prev = nodes[idx - 1]
        nxt = nodes.get(idx + 1, None)

        if prev == None:
            return head.next
        
        prev.next = nxt
        return head

