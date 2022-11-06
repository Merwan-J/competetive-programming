class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        """
        
        since i<j, the j-i is always a positive number
        
        instead of counting the bad pairs what if we count the good pairs
        good pairs: i<j and j-i == nums[j]-nums[i]
        
        then our answer will be the (totalpairs - goodpairs)
        
        how do we count the goodpairs??
        
        nums[j]-nums[i] = j - i, we can rearrange the equation
        
        j-nums[j] = i - nums[i]
        
        so for each index i, we will look for prev index position that equals i - nums[i]
        
        how many total pairs are there??
        0 : 3
        1 : 2
        2 : 1
        3 : 0
        
        n-1 + n - 2 + n-3 + 0
        
        we know the formula for sum of n consecative integers
        
        sum(n integers) = n + n- 1 + n-2 + n- 3 .. 0
        
        sum(n integers) = n(n+1)/2
        
        but we need to modify this formula, since we dont want to inculde n in our sum
        
        n(n+1)/2 - n -> our formula
        
        """
        
        
        
#         intialize vars: goodpairs, lookup, total pairs
        n = len(nums)
        goodpairs = 0
        totalpairs = (n*(n+1)//2) - n
        lookup = defaultdict(int)
        
#          count the good pairs
        for i,num in enumerate(nums):
            target = i - nums[i]
            if target in lookup:
                goodpairs+=lookup[target]
            lookup[target]+=1
#          find the bad pairs: totalpairs-goodpairs
        return totalpairs-goodpairs