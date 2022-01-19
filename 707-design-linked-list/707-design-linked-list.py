class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next



class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if self.length == 0:
            return -1
        else:
            crntNode = self.head
            for i in range(index):
                if crntNode == None:
                    return -1
                crntNode = crntNode.next
            return crntNode.val if crntNode != None else -1

    def addAtHead(self, val: int) -> None:
        node = Node(val,self.head)
        self.head = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.length == 0:
            self.head = node
            self.length += 1
        else:    
            crntNode = self.head
            while crntNode.next:
                crntNode = crntNode.next
            crntNode.next = node
            self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            return self.addAtHead(val)
        elif index == self.length:
            return self.addAtTail(val)
        elif self.length and index<self.length:
            crntNode = self.head
            for i in range(index-1):
                crntNode = crntNode.next
            crntNode.next = Node(val,crntNode.next)
            self.length += 1
            
    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.length:
            self.head = self.head.next
            self.length -= 1
        elif self.length and index<self.length:
            crntNode = self.head
            for i in range(index-1):
                crntNode = crntNode.next 
            crntNode.next = crntNode.next.next
            self.length -= 1
                
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)