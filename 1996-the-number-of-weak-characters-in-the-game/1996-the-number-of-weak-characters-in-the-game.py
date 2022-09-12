class Solution:
    def numberOfWeakCharacters(self, arr: List[List[int]]) -> int:
        arr.sort(key=lambda item: (item[0],-item[1]))
        stack = []
        count = 0
        
        for attack,defense in arr:
            while stack and stack[-1][0]<attack and stack[-1][1]<defense:
                stack.pop()
                count += 1
            stack.append((attack,defense))
        
        return count