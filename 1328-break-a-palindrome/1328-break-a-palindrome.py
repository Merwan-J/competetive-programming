class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1: return ""
        
        first = [i for i in palindrome[:len(palindrome)//2]]
        second = [i for i in palindrome[len(palindrome)//2:]]
        
        print(first,second)
        
        for i in range(len(first)):
            if first[i] != 'a':
                first[i] = 'a'
                return ''.join(first+second)
        
        for i in range(len(second)):
            if second[i] != 'a' and not (len(palindrome)%2 and i!=len(palindrome)//2):
                second[i] = 'a'
                return ''.join(first+second)
        
        second[-1] = 'b'
        return ''.join(first+second)
                