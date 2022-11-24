class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
#         what is the question asking?
#         -build a a subsequence that results a maximum sum but each consequ. elts are at most k pos apart
        
#         typical dp on subsequence
        
#         i can ask myself what is the maximum sum I can build from this position
        
#         i have two chioces to make: either to start a new subsequence or continue what I have previously built 
            
        
            
#         start a new subsequence: just include the current num, nums[i]
#         continue: i can choose any previous max sum then return max(nums[i]+prevmax,prevmax)
        
#         then dp[i] = max(startnewsub, continue)
#             dp[i] = max(nums[i],nums[i]+prevMax,prevMax)
        
#         I think in the relation putting prevMax results a probelm 
#         prove: here u go
#         [10,2,-10,-5,-20] k =2
        
#         [10,10,10,10,10] max sum for each window
            
        
#         so I need to change the way I am looking at the probelm because the realtion doesn't           work specially the prevMax thing
        
#         so if instead think of dp[i] as the maxsum of a valid subsequence that is ending at           this given position including the current number, nums[i]. this way we can prevent             cases where prevMax wont include sum out of our k sized window
        
#         [10]
#         [0]
        
#         [10,8]
#         [10,10]
        
#         [10,8,-2]
#         [10,8,8]
#         [10,10,0]
        
#         [10,8,-2,-7]
#         [10,8,8,3]
#         [10,10,0,-5]
        
        
#         i will need a heap to get me the valid max sum in logn time 
#         I will pop from the heap if the max is not in the k sized window 
#         1D dp array to store the max sum in each position 
        
        n = len(nums)
        heap = [(-nums[0],0)]
        dp = [0]*n
        dp[0] = nums[0]
        
        
        # for i in range(1,n):
        #     while heap[0][1]<(i-k):
        #         heappop(heap)
        #     dp[i] = nums[i] + max(0,-heap[0][0])
        #     heappush(heap,(-dp[i],i))
        
        dq = deque([0])
        for i in range(1,n):
            num = nums[i]
            while dq[0]<i-k:
                dq.popleft()
            dp[i] = num + max(0,dp[dq[0]])
            
            while dq and dp[i]>dp[dq[-1]]:
                dq.pop()
            dq.append(i)

        return max(dp)
        
        
        
        