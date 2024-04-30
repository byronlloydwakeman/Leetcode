# Working solution however times out on the 48th test case when submitted
# Has a time complexity of O(n^3) (oof)
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        def is_wonderful(word):
            dict_letters = {}

            for letter in word:
                try:    
                    dict_letters[letter] += 1
                except KeyError as e:
                    dict_letters[letter] = 1
                    
            # Find count of odd numbers
            count = 0
            for key in dict_letters.keys():
                if dict_letters[key] % 2 != 0:
                    count += 1
            
            if count <= 1:
                return True
            else:
                return False

        temp_wonderful_string = ""
        count = 0
        index = 0
        # Try and go through all combinations
        for i in range(len(word)):
            for letter in word[i:]:
                temp_wonderful_string += letter
                if temp_wonderful_string == "":
                    count += 1
                else:
                    if is_wonderful(temp_wonderful_string):
                        count += 1
            temp_wonderful_string = ""
        
        return count


