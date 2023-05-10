class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ''.join(list(map(str, digits)))
        number = int(number) + 1
        return list(map(int, str(number)))