class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash = dict()
        
        for i in range(len(numbers)):
            if target-numbers[i] in hash:
                return [hash[target-numbers[i]]+1,i+1]
            hash[numbers[i]] = i
            