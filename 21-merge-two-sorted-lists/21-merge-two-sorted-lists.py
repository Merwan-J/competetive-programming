# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None or list2==None:
            ans = list1 if list1!=None else list2
            return ans
        
        arr = []
        
        while list1 or list2:
            if list1:
                arr.append(list1)
                list1 = list1.next
            if list2:
                arr.append(list2)
                list2 = list2.next
        
        arr = sorted(arr,key=lambda node: node.val)
        
        for i in range(len(arr)):
            if i == len(arr)-1:
                arr[i].next = None
                continue
            
            node = arr[i]
            node.next = arr[i+1]
        # print(arr[0])
        return arr[0]
            