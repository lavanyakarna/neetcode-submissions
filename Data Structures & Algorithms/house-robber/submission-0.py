class Solution:
    def rob(self, nums: List[int]) -> int:
        one=0
        two=0
        for money in nums:
            temp=one
            one=max(one,money+two)
            two=temp
        return one
        