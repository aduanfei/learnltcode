class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        print(nums)
        res = dif = float("inf")
        for i in range(len(nums) - 2):
            l = i + 1
            k = len(nums) - 1
            while (l < k):
                sum1 = nums[i] + nums[l] + nums[k]
                dif2 = abs(sum1 - target)
                if dif2 < dif:
                    dif = dif2
                    res = sum1
                if sum1 >=target:
                    k -= 1
                elif sum1 < target:
                    l += 1

        return res

s=Solution()
print(s.threeSumClosest([1,1,1,0],-100))