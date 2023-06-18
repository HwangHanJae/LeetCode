class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        while nums:
            a = nums.pop()
            b = nums.pop()
            result += min(a,b)
        return result