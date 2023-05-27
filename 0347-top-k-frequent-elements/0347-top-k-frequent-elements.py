class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        result = []
        for num in nums:
            d[num] = d.get(num, 0) + 1
        items = sorted(d.items(), key=lambda x : x[1], reverse=True)
        for i in range(k):
            element, frequent = items[i]
            result.append(element)
        return result
            