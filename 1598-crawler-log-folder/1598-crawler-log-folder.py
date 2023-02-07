class Solution:
    def minOperations(self, logs: List[str]) -> int:
        goToParent = "../"
        stayThere = "./"
        level = 0
        
        for log in logs:
            if log != goToParent and log != stayThere:
                level+=1
            elif log == goToParent and level>0:
                level-=1
        
        return level