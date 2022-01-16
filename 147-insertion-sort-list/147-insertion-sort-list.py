# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        nodes = []
        
        while head:
            nodes.append(head)
            head = head.next

        for j in range(1,len(nodes)):
            crntMin = (j,nodes[j])
            _index = crntMin[0] -1
            while _index >= 0 and crntMin[1].val < nodes[_index].val:
                nodes[crntMin[0]] = nodes[_index]
                nodes[_index] = crntMin[1]
                crntMin = (_index,crntMin[1])
                _index -= 1
                
        for i in range(len(nodes)-1):
            if i+1 == len(nodes)-1:
                nodes[i+1].next = None      
            nodes[i].next = nodes[i+1]
        
        return nodes[0]
            