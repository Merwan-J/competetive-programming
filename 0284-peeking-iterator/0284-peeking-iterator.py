# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator: Iterator):
        self.iterator = iterator
        self.move()
            
    def move(self) -> None:
        if self.iterator.hasNext():
            self.next_num = self.iterator.next()
        else:
            self.next_num = None

    def peek(self) -> int:
        return self.next_num
        
    def next(self) -> int:
        next_num = self.next_num
        self.move()
        return next_num
        
    def hasNext(self) -> bool:
        return self.next_num is not None
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].