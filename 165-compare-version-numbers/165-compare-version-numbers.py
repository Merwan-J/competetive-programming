class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1 = v1.split('.')
        v2 = v2.split('.')
        
        v1 = list(map(int,v1))
        v2 = list(map(int,v2))
        
        # print(v1,v2)
        
        while len(v1)<len(v2):
            v1.append(0)
        
        while len(v2)<len(v1):
            v2.append(0)
            
        for i in range(len(v1)):
            if v1[i]<v2[i]:
                return -1
            elif v2[i]<v1[i]:
                return 1
        
        return 0