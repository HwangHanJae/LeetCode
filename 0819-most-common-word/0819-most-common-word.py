import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dic = {}
        for c in "!?',;.":
            paragraph = paragraph.replace(c, ' ')
        
        for word in paragraph.split():
            word = word.lower().strip()
            if word not in banned:
                dic[word] = dic.get(word, 0) + 1
        results = sorted(dic.items(), key=lambda x : x[1], reverse=True)
        result = results[0][0]
        return result