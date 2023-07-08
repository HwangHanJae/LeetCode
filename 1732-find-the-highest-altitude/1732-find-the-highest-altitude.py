class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = 0
        result = 0
        for i in gain:
            prefix_sum += i
            result = max(prefix_sum, result)
        return result