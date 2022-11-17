class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        difference = []
        negatives = []
        n = len(cost)
        for i in range(n):
            difference.append(gas[i]-cost[i])
            
        circular_diff = []
        for i in range(2*n):
            cur_diff = difference[i%n]
            prev = 0 if i == 0 else circular_diff[-1]
            if prev>=0:
                circular_diff.append(prev+cur_diff)
            else:
                circular_diff.append(cur_diff)



        count = 1 if circular_diff[0] <0 else 0
        negatives.append(count)
        
        for i in range(1,2*n):
            add = 0 if circular_diff[i] >=0 else 1
            negatives.append(negatives[-1] + add)
        # print(circular_diff)
        # print(negatives)
        for i in range(n):
            start = i
            end = i + n-1

            if circular_diff[start]>=0 and negatives[end] - negatives[start] == 0:
                return start
        
        return -1
