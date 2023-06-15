class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            result += list(str(num))
        
        return list(map(int, result))