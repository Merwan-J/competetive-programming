class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        prevChar = chars[0]
        count = 1
        insertPos = 1 
        
        for i in range(1,n):
            curChar = chars[i]
            
            if curChar!=prevChar:
                prevChar = curChar
                insertPos += len(str(count)) + 1 if count>1 else 1
                chars[insertPos-1] = curChar
                count = 1 
                continue 
            
            count+=1            
            for j in range(len(str(count))):
                chars[insertPos+j] = str(count)[j] 
                
        return insertPos + len(str(count)) if count > 1 else insertPos