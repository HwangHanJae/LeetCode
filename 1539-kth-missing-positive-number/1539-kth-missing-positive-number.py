class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        all_numbers = set([i for i in range(1, 2001) if i not in arr])
        result = list(set(all_numbers) - set(arr))
        return result[k-1]
        
        