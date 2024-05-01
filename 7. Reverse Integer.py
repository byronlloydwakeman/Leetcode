class Solution:
    def reverse(self, x: int) -> int:
        if len(str(x)) == 1:
            return x

        is_negative = False
        if x < 0:
            is_negative = True
        string_x = str(x)

        reverse_string = string_x[::-1]
        zero_char = reverse_string[0]
        while zero_char == "0":
            # Remove the first item
            reverse_string = reverse_string[1:]
            zero_char = reverse_string[0]

        result = int(reverse_string) if not is_negative else int(reverse_string[:-1]) * -1

        if result <= -2**31 or result >= 2**31 - 1:
            return 0

        return result
