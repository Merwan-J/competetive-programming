class Solution:
    def findBestValue(self, nums: List[int], target: int) -> int:
        nums.sort()
        p_sum = [0]
        # print(nums)
        for num in nums:
            p_sum.append(num + p_sum[-1])
        # print(p_sum)
        def check(num):
            l = 0
            r = len(nums) -1

            ans = r+1
            while l<=r:
                mid = l + (r-l)//2
                if nums[mid] >= num:
                    ans = mid
                    r= mid-1
                else:
                    l = mid+1

            # print(num*(len(nums)-ans) + p_sum[ans], num)
            return num*(len(nums)-ans) + p_sum[ans]

        

        ans = float('inf')
        ans_num = 0

        l = 0
        r = max(nums)

        while l<=r:
            mid = l + (r-l)//2

            found = check(mid)
            cur = abs(target - found)

            if cur < ans:
                ans = cur
                ans_num = mid
            if cur == ans:
                ans_num = min(ans_num, mid)
            if found >= target:
                r = mid-1
            elif found < target:
                l = mid + 1

        return (ans_num)


