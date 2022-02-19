class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        arr = strs[::]
        
        for i in range(len(strs)):
            strs[i] = sorted(strs[i])
        
        
        for i in range(len(strs)):
            strs[i] = ("".join(strs[i]),i)
        
        
        strs.sort()
        
        ans = [[]]
        prev = strs[0][0]
        for word in strs:
            if prev != word[0]:
                ans.append([])
                prev = word[0]
            ans[-1].append(arr[word[1]])
                
            
        return ans
            
