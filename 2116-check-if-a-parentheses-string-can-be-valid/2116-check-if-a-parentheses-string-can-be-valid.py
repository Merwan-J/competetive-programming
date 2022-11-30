class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
#         how to know if the prefix is invalid?
#             when the number of closers is greater than the number of openers
#             - when the numbers of closers are greater at any time, try changing, if it locked return True
        
#         at the end what if I have greater number of openers than closers?
#             start iterating from the top of the stack and try to balance them, if need to swap but it is               locked I need to return False
#         (( ))
#         ()()()
#         ((( )))
#         (((((( -> (( )) ()

        # ((((
    
        def check(s,locked,brace):
            balance = 0
            
            for i,char in enumerate(s):
                if locked[i] == "0" or char == brace:
                    balance += 1
                else:
                    balance -= 1
                if balance<0: return False
            
            return True
    
        return len(s)&1 == 0 and check(s,locked,"(") and check(s[::-1],locked[::-1],")")                    
        
        