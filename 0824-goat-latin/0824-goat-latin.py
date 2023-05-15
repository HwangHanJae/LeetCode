from collections import deque
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        result = []
        for i, word in enumerate(sentence.split()):
            word = deque(word)
            if word[0].lower() not in ['a', 'e', 'i', 'o', 'u']:
                p = word.popleft()
                word.append(p)
            word = ''.join(list(word))
            new = word + 'ma' + 'a' * (i+1)
            
            result.append(new)
                
                
        
        return ' '.join(result)