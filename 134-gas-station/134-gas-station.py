class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net = 0
        start = 0
        rungas = 0
        
        for i in range(len(gas)):
            net += gas[i]-cost[i]
            rungas += gas[i] - cost[i]
            
            if rungas<0:
                rungas = 0
                start = i+1
        
        return -1 if net<0 else start
