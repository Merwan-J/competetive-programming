def numIdenticalPairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i] == nums[j] and i<j:
                count+=1
    return count

