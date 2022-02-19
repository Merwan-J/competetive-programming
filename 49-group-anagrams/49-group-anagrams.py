class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        arr = strs[::]
        ans = [[]]
        for i in range(len(strs)):
            strs[i] = sorted(strs[i])
        
        
        for i in range(len(strs)):
            strs[i] = ("".join(strs[i]),i)
        
        
        strs.sort()
        
        prev = strs[0][0]
        for word in strs:
            if prev == word[0]:
                ans[-1].append(arr[word[1]])
            else:
                ans.append([])
                ans[-1].append(arr[word[1]])
                prev = word[0]
            
        return ans
            