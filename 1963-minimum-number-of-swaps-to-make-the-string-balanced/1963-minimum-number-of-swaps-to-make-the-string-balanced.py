class Solution:
    def minSwaps(self, s: str) -> int:
        
        
#             I know how to swap and where to swap
            
#             but after I make my swap how do I know if the current prefix is valid??
            
#             since there always exits a closer for each opener in the string
#             I know that a prefix string is valid if the number of openers are greater or equal to the number of closers in that prefix
            
#             if this is the case that means it is valid so I wont make any swaps, I will just continue.
        
        
        
#             how to keep track of the closers and openers in the prefix
#             if the prefix is valid just count what ever is the current char
            
#             if the prefix is in valid, swap and count
            
#             having opener in the front is not a problem but having a closer in the front is a big problem             since it wont ever be valid 
            
            # [[]]]][[
        
        openers_pos = []
        s = [char for char in s]
        
        for i,char in enumerate(s):
            if char == "[":
                openers_pos.append(i)
        
        balance = 0
        count = 0
        
        for i in range(len(s)):
            char = s[i]
            add = 1 if char == "[" else -1
            
            # it still is valid dont make a swap
            if balance + add >=0:
                balance+=add
            else:
                s[i],s[openers_pos.pop()] = s[openers_pos[-1]], s[i]
                balance+=1
                count+=1
        
        return count
                
        
        # ]]][[[
        # [][[]]   
        
            