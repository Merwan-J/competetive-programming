class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def isps(a):
            b=int(sqrt(a))
            return b*b==a
        ct=Counter(nums)
        cand={}
        for a in ct:
            cand[a]={b for b in ct if isps(a+b)}
        ##
        n=len(nums)
        def dfs(x, left=n-1):
            count=0
            ct[x]-=1
            if left==0:
                count=1
            else:
                for y in cand[x]:
                    if ct[y]>0:
                        count+=dfs(y,left-1)
            ct[x]+=1
            return count
        ##
        res=0
        for x in ct:
            res+=dfs(x,n-1)
        return res
        