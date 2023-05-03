class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        targetSet = set(target)
        output = []
        
        for num in range(1,n+1):
            
            if num>target[-1]:
                break
            
            output.append("Push")
            if num not in targetSet:
                output.append("Pop")
        
        
        return output            