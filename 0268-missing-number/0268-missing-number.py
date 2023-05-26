class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        numbers = set(i for i in range(n+1))
        result = numbers - set(nums)
        
        return list(result)[0]