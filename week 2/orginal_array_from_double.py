class Solution:
    def findOriginalArray(self, li: List[int]) -> List[int]:
            li = sorted(li)
            d = {}
            new_li = []
            if len(li)%2 !=0:
                return []
            
            for i in li:
                if i not in d:
                    d[i] = 1
                else:
                    d[i]+=1
            for key in li:
                if key!=0 and key*2 in d and d[key] and d[key*2]:
                    new_li.append(key)
                    d[key] -= 1
                    d[key*2] -= 1
                if key ==0 and d[key]>=2:
                    new_li.append(key)
                    d[key] -= 2
                if len(new_li) == len(li)/2:
                    return new_li
                

            return []
            
              
