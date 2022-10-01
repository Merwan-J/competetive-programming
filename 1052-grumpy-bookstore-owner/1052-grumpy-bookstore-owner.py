class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        already_satisfied = 0
        prefix = [0]*len(customers)
        prefix[0] = 0 if grumpy[0] == 0 else customers[0]

        for idx, customer in enumerate(customers):
            if grumpy[idx] == 0:
                already_satisfied += customer

        for idx in range(1, len(customers)):
            if grumpy[idx] == 1:
                prefix[idx] = prefix[idx-1] + customers[idx]
            else:
                prefix[idx] = prefix[idx-1]

        ans = 0
        for idx in range(len(prefix)):
            
            total_idx = idx + minutes - 1
            right_part = prefix[total_idx] if total_idx < len(prefix) else 0
            left_part = prefix[idx-1] if idx - 1 >= 0 else 0
            ans = max(ans, right_part-left_part)

        return ans + already_satisfied
