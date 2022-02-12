class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        
        hashMap = {}
        count = 1
        
        for num in nums:
            hashMap[num] = hashMap.get(num,0) + 1
        hashMap = dict(sorted(hashMap.items(),key=lambda item: item[1],reverse=True))
        print(hashMap)
        arr = []
        for key,value in hashMap.items():
            arr.append(key)
            if len(arr)==k:
                return arr
        