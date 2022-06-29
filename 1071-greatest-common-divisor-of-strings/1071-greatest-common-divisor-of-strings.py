class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
#         using Euclidean algorithm for gcd of numbers to Strings
        
        def gcd(s1,s2):
            if len(s1)<len(s2):
                return gcd(s2,s1)
            
            if s2=="":
                return s1
            
            if s1[:len(s2)] == s2:
                return gcd(s1[len(s2):],s2)
            return ""
        
        return gcd(str1,str2)

       