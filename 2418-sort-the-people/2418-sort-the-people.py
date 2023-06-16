class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = [(name, height) for name,height in zip(names, heights)]
        people.sort(key=lambda x : x[1], reverse=True)
        
        return [name for name, height in people]
        