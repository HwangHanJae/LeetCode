from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numbers = set(arr)
        counter = Counter(arr)
        count = [counter[number] for number in numbers]
        count = sorted(tuple(count))
        compare = sorted(tuple(set(count)))
        if count== compare:
            return True
        else:
            return False