class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        print(nums)
        res=[]
        for i in range(len(nums)-2):
            l=i+1
            k = len(nums) - 1
            while(l<k):
                sum1=nums[i]+nums[l]+nums[k]
                if sum1>0:
                    k-=1
                elif sum1<0:
                    l+=1
                else:
                    temp=[nums[i],nums[l],nums[k]]
                    if not temp in res:
                        res.append(temp)
                    k-=1
        return res

s=Solution()
print(s.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))