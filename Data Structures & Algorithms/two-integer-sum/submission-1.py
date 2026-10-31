class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,j in enumerate(nums):
            diff=target-j
            if diff in d:
                return [d[diff],i]
            d[j]= i
        