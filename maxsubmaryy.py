# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maxsub=nums[0]
#         sum=0
#         for i in nums:
#             if sum<0:
#                 sum=0
#             sum+=i
#             maxsub=max(maxsub,sum)
#         return maxsub


def maxSubArray( nums):
        maxsub=nums[0]
        sum=0
        for i in nums:
            if sum<0:
                sum=0
            sum+=i
            maxsub=max(maxsub,sum)
        return maxsub
print( maxSubArray([-2,1,-3,4,-1,2,1,-5,4] ))