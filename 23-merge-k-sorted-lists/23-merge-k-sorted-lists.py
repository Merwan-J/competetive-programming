# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        arr = []
        
        for list in lists:
            while list:
                arr.append(list)
                list = list.next
        
        arr.sort(key=lambda node: node.val)
        if arr==[]:
            return None
        for i in range(1,len(arr)):
            arr[i-1].next = arr[i]
        
        return arr[0]