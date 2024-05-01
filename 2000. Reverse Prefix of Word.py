class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)

        if index == -1:
            return word
        
        substring = word[:index + 1]
        substring_reverse = substring[::-1]

        return substring_reverse + word[index + 1:]

