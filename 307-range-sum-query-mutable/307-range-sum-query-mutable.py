class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.arr = nums
        self.seg = [0]*(4*self.n)
        
        def build(low,high,ind):
            if low == high:
                self.seg[ind] = self.arr[low]
                return
            
            mid = low + (high-low)//2
            
            left = 2*ind+1
            right = 2*ind+2
            
            build(low,mid,left)
            build(mid+1,high,right)
            self.seg[ind] = self.seg[left] + self.seg[right]
        build(0,self.n-1,0)
            
    def update(self, index: int, val: int) -> None:
        def update(low,high,ind,index,val):
            if low==high==index:
                self.arr[index] = val
                self.seg[ind] = val
                return
            if low>index or high<index:
                return
            
            mid = low + (high-low)//2
            
            left = 2*ind + 1
            right = 2*ind + 2
            
            update(low,mid,left,index,val)
            update(mid+1,high,right,index,val)
            self.seg[ind] = self.seg[left] + self.seg[right]
        update(0,self.n-1,0,index,val)

    def sumRange(self, left: int, right: int) -> int:
        def query(low,high,ind,l,r):
            if low>=l and high<=r:
                return self.seg[ind]
            if low>r or high<l:
                return 0
            mid = low + (high-low)//2
            left = 2*ind + 1
            right = 2*ind + 2
            
            return query(low,mid,left,l,r) + query(mid+1,high,right,l,r)
        
        return query(0,self.n-1,0,left,right)
            
            
            
            


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)