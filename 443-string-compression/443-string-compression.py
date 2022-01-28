class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return 1
        
        s = ""
        l,r=0,1
        count = 1
        
        while r<=len(chars):
            if r==len(chars) or chars[l]!=chars[r]:
                s+= chars[l] if count==1 else chars[l]+str(count)
                count = 0 
                l = r
            count+=1
            r+=1
            
        for j in range(len(s)):
            if j >=len(chars):
                chars.append(s[j])
            else:
                chars[j]=s[j]
            
        while len(chars)>len(s):
            chars.pop()
            
        return len(chars)