class Solution:
    def tribonacci(self, n: int) -> int:
        # Edge cases
        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        def recursion(n):
            nonlocal index
            nonlocal prev_2
            nonlocal prev_1
            nonlocal prev_3
            nonlocal cur
            
            # Base cases
            if index == 0:
                cur = 0
                prev_1 = 1
                prev_2 = 1
                index += 1
                return recursion(n)
            elif index == 1:
                cur = 1
                prev_2 = 1
                index += 1
                return recursion(n)
            elif index == 2:
                cur = 1
                index += 1
                return recursion(n)

            # Calculate current value using previous three values
            cur = prev_1 + prev_2 + prev_3
            prev_3, prev_2, prev_1 = prev_2, prev_1, cur

            index += 1

            # Check if reached desired n
            if index - 1 == n:
                return cur

            # Recurse
            return recursion(n)

        # Initialize variables
        index = 0
        prev_3 = 0
        prev_2 = 0
        prev_1 = 0
        cur = 0

        return recursion(n)
