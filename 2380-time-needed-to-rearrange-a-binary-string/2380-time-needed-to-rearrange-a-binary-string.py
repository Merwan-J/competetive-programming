class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        seconds = 0
        
        while '01' in s:
            seconds += 1
            s = s.replace('01', '10')
            
        return seconds