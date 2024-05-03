class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_int = ""
        for digit in digits:
            str_int += str(digit)

        int_int = int(str_int)

        int_int += 1

        to_return = []
        for char in str(int_int):
            to_return.append(int(char))

        return to_return
        
