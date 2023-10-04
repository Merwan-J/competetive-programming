class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate_one, candidate_two, count_one, count_two = -1,-1,0,0
        
        for num in nums:
            if num == candidate_one:
                count_one+=1
            elif num == candidate_two:
                count_two+=1
            elif count_one==0:
                candidate_one = num
                count_one=1
            elif count_two==0:
                candidate_two = num
                count_two=1
            else:
                count_one-=1
                count_two-=1
        
        return set([ num for num in (candidate_one,candidate_two)  if nums.count(num)> len(nums)//3 ])