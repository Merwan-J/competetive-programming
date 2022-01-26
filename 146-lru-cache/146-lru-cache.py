class ListNode:
    def __init__(self,key,value,next=None,prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.oldNode = None
        self.newNode = None
    
    def add_new(self,key,value):
        node = ListNode(key,value,None,self.newNode)
        if len(self.cache)==0:
            self.oldNode = node
            self.newNode = node
        else:
            self.newNode.next, self.newNode = node,node
        self.cache[key] = node
    
    def remove_old(self,key,value):
        self.cache.pop(self.oldNode.key)
        self.oldNode = self.oldNode.next
        node = ListNode(key,value,None,self.newNode)
        self.newNode.next,self.newNode = node,node
        self.cache[key] = node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            if self.capacity == 1 or len(self.cache)==1:
                return self.cache[key].value
            node = self.cache[key]
            if node == self.oldNode:
                self.oldNode = self.oldNode.next
                self.newNode.next, node.prev = node,self.newNode
                self.newNode = node
            elif node == self.newNode:
                pass
            else:
                node.prev.next, node.next.prev = node.next,node.prev
                self.newNode.next,node.prev,self.newNode = node,self.newNode,node
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        print("put")
        if key in self.cache:
            print("key in cache,updating")
            node = self.cache[key]
            node.value = value
            if self.capacity ==1 or len(self.cache)==1:
                pass
            elif node==self.newNode:
                pass
            elif node == self.oldNode:
                self.oldNode = self.oldNode.next
                self.newNode.next, node.prev, self.newNode = node,self.newNode, node
            else:
                node.prev.next, node.next.prev = node.next, node.prev
                self.newNode.next, node.prev, self.newNode = node,self.newNode,node
        else:
            if self.capacity == len(self.cache):
                if self.capacity ==1:
                    node = ListNode(key,value,None,None)
                    self.cache.pop(self.oldNode.key)
                    self.oldNode,self.newNode = node,node
                    self.cache[key] = node
                    return None
                    
                self.remove_old(key,value)
            else:
                self.add_new(key,value)


