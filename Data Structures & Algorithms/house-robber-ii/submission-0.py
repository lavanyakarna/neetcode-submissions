class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        def rob_line(nums):
            one=0
            two=0

            for money in nums:
                temp=one
                one=max(one,money+two)
                two=temp
            return one
        return max((rob_line(nums[1: ]),(rob_line(nums[ :-1]))))
        